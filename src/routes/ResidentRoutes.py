from flask import Blueprint, jsonify, request
from utils.field_validation import Fiel_validation
from controllers.ResidentController import ResidentController
from utils.response_utils import Response
import uuid

#Models
from models.ResidentModel import ResidentModel

main=Blueprint('resident_blueprint',__name__)

# para ver los reesultados de las paginaciones agregue ?page=2 a la URL
@main.route('/', methods=['GET'])
def get_residents():
    
    try:
        page = request.args.get('page', 1, type=int)
        per_page = 10
        residents = ResidentController.get_residents(page=page, per_page=per_page) 
        return jsonify(Response.success_response("Operation completed successfully",residents))

    except Exception as ex:
        return jsonify(Response.error_response("Error retrieving data",status_code=500, error_details=str(ex))),500
    

@main.route('/<parameter>', methods=['GET'])
def get_resident(parameter):
    try:
        page = request.args.get('page', 1, type=int)
        per_page = 10

        residents = ResidentController.search_residents(parameter,page=page, per_page=per_page)
        if residents is not None:    
            return jsonify(Response.success_response("Operation completed successfully",residents))
        else:
            return jsonify({}),404
        
    except Exception as ex: 
        return jsonify(Response.error_response("Error retrieving data",status_code=500,error_details=str(ex))),500


@main.route('/add', methods=['POST'])
def add_resident():

    try:
        id = str(uuid.uuid4())
        name = request.json['name']
        last_name = request.json['last_name']
        phone = request.json['phone']
        email = request.json['email']
        age = request.json['age']
        address = request.json['address']
        delivered_food = request.json['delivered_food']
        observation = request.json['observation']
        
        #validacion de los datos
        if not Fiel_validation.validate_name(name):
            return jsonify(Response.error_response("Invalid name",status_code=400,error_details=str(ex))),400

        if not Fiel_validation.validate_last_name(last_name):
            return jsonify(Response.error_response("Invalid last name",status_code=400,error_details=str(ex))),400
        
        if not Fiel_validation.validate_phone(phone):
            return jsonify(Response.error_response("Invalid phone",status_code=400,error_details=str(ex))),400
        
        if not Fiel_validation.validate_email(email):
            return jsonify(Response.error_response("Invalid email",status_code=400,error_details=str(ex))),400

        if not Fiel_validation.validate_age(age):
            return jsonify(Response.error_response("Invalid age",status_code=400,error_details=str(ex))),400
        
        if not Fiel_validation.validate_address(address):
            return jsonify(Response.error_response("Invalid address",status_code=400,error_details=str(ex))),400
        
        if not Fiel_validation.validate_delivered_food(delivered_food):
            return jsonify(Response.error_response("Invalid delivered_food",status_code=400,error_details=str(ex))),400

        if not Fiel_validation.validate_observation(observation):
            return jsonify(Response.error_response("Invalid observation",status_code=400,error_details=str(ex))),400

        resident = ResidentModel(id, name, last_name, phone, email, age, address, delivered_food, observation)
        
        affected_row = ResidentController.add_resident(resident)

        if affected_row:
            return jsonify(Response.success_response("Operation completed successfully",affected_row))

        else:
            return jsonify(Response.error_response("Error or insert",status_code=500,error_details=str(ex))),500

    except Exception as ex:
        return jsonify(Response.error_response("Error or insert",status_code=500,error_details=str(ex))),500
    

@main.route('/delete/<id>', methods=['DELETE'])
def delete_resident(id):
    try:
        resident = ResidentModel(id)
        affected_row = ResidentController.delete_resident(resident) 

        if affected_row:    
            return jsonify(Response.success_response("Operation completed successfully",resident.id))
        else:
            return jsonify(Response.error_response("No Resident deleted",status_code=400,error_details=str(ex))),400

    except Exception as ex:
        return jsonify(Response.error_response("Error or delete",status_code=500,error_details=str(ex))),500


@main.route('/updated/<id>', methods=['PUT'])
def update_resident(id):

    try:
        if id != request.json.get('id'):
            return jsonify({'message': 'Changing the ID is not allowed'}), 400
        
        name = request.json['name']
        last_name = request.json['last_name']
        phone = request.json['phone']
        email = request.json['email']
        age = request.json['age']
        address = request.json['address']
        delivered_food = request.json['delivered_food']
        observation = request.json['observation']

        if not Fiel_validation.validate_name(name):
            return jsonify(Response.error_response("Invalid name",status_code=400,error_details=str(ex))),400

        if not Fiel_validation.validate_last_name(last_name):
            return jsonify(Response.error_response("Invalid last name",status_code=400,error_details=str(ex))),400
        
        if not Fiel_validation.validate_phone(phone):
            return jsonify(Response.error_response("Invalid phone",status_code=400,error_details=str(ex))),400
        
        if not Fiel_validation.validate_email(email):
            return jsonify(Response.error_response("Invalid email",status_code=400,error_details=str(ex))),400

        if not Fiel_validation.validate_age(age):
            return jsonify(Response.error_response("Invalid age",status_code=400,error_details=str(ex))),400
        
        if not Fiel_validation.validate_address(address):
            return jsonify(Response.error_response("Invalid address",status_code=400,error_details=str(ex))),400
        
        if not Fiel_validation.validate_delivered_food(delivered_food):
            return jsonify(Response.error_response("Invalid delivered_food",status_code=400,error_details=str(ex))),400

        if not Fiel_validation.validate_observation(observation):
            return jsonify(Response.error_response("Invalid observation",status_code=400,error_details=str(ex))),400
        
        resident = ResidentModel(id, name, last_name, phone, email, age, address, delivered_food, observation)
        affected_row = ResidentController.update_resident(resident)

        if affected_row:
            return jsonify(Response.success_response("Operation completed successfully",resident.id))
        else:
            return jsonify({'message': "No resident updated"}),500

    except Exception as ex:
        return jsonify(Response.error_response("Error or updated",status_code=500,error_details=str(ex))),500
    

#Ordena los datos por edad  de forma descendente
@main.route('/order/age', methods=['GET'])
def filter_by_age_descending():
    try:
        page = request.args.get('page', 1, type=int)
        per_page = 10
        residents = ResidentController.filter_by_age_descending(page=page, per_page=per_page)   
        return jsonify(Response.success_response("Operation completed successfully",residents))

    except Exception as ex:
        return jsonify(Response.error_response("Error retrieving data",status_code=500,error_details=str(ex))),500  
    

#Ordena los datos por nombre  de forma ascendente
@main.route('/order/name', methods=['GET'])
def filter_by_name_ascending():

    try:
        page = request.args.get('page', 1, type=int)
        per_page = 10
        residents = ResidentController.filter_by_name_ascending(page=page, per_page=per_page)   
        return jsonify(Response.success_response("Operation completed successfully",residents))

    except Exception as ex:
        return jsonify(Response.error_response("Error retrieving data",status_code=500,error_details=str(ex))),500