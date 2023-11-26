from flask import Flask
from flask_cors import CORS
# from config import config

#Routes
from routes import ResidentRoutes

from models.ResidentModel import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost:5432/python_flask_rest_api'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Deshabilita la modificación del seguimiento para mejorar el rendimiento


db.init_app(app)

#habilita la posibilidad de consumir la api desde otras rutas, especificando la ruta
CORS(app, resources={"*":{"origins": "http:///localhost:3000"}})


def page_not_found(error):
    return "<h1>Page not found</h1>"

if __name__ == ('__main__'):
    # app.config.from_object(config['development'])

    #Blueprints
    app.register_blueprint(ResidentRoutes.main, url_prefix='/api/residents')

    #Error handler
    app.register_error_handler(404,page_not_found)
    app.run(debug=True)