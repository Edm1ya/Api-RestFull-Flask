from flask import Flask
from flask_cors import CORS
from models.ResidentModel import db
from flask_migrate import Migrate
import config

#Routes
from routes import ResidentRoutes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Deshabilita la modificación del seguimiento para mejorar el rendimiento


db.init_app(app)
migrate = Migrate(app, db)

#habilita la posibilidad de consumir la api desde otras rutas, especificando la ruta
CORS(app, resources={"*":{"origins": "http:///localhost:3000"}})


def page_not_found(error):
    return "<h1>Page not found</h1>"

#Crea la base de datos si no existe
with app.app_context():
    db.create_all()

if __name__ == ('__main__'):
    
    #Blueprints
    app.register_blueprint(ResidentRoutes.main, url_prefix='/api/residents')

    #Error handler
    app.register_error_handler(404,page_not_found)

    app.run(debug=True)