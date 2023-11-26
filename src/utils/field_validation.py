import re

class Fiel_validation():

    @classmethod
    def validate_name(self, name):
        if len(name) <= 50:
            return True
        return False
    
    @classmethod
    def validate_last_name(self, last_name):
        if len(last_name) <= 50:
            return True
        return False
    
    @classmethod
    def validate_phone(self, phone):
        if len(str(phone)) == 10 :
            return True
        return False
    
    @classmethod
    def validate_email(self, email):
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email) is not None

    @classmethod
    def validate_age(self, age):
        if int(age) > 0 and int(age) < 120:
            return True
        return False
    
    @classmethod
    def validate_address(self, address):
        if len(address) <= 70:
            return True
        return False

    def validate_delivered_food(delivered_food):
        if delivered_food == True or delivered_food == False:
            return True
        return False
        

    def validate_observation(observation):
        if len(observation) <= 500:
            return True
        return False