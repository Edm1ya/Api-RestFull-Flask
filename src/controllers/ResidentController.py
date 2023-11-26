from models.ResidentModel import ResidentModel, db
from sqlalchemy import text


class ResidentController():
    
    @classmethod
    def get_residents(self,page, per_page):
        try:
            residents =[]
            resultset = ResidentModel.query.order_by(ResidentModel.created_at.asc()).paginate(page=page, per_page=per_page, error_out=False)

            for resident in resultset.items:
                residents.append(resident.to_JSON())

            return residents

        except Exception as ex:
            raise Exception( ex)
        
    @classmethod
    def search_residents(self, target, page, per_page):
        try:
            residents =[]
            # Realizar una consulta en la base de datos
            resultset = ResidentModel.query.filter(
                (ResidentModel.id.ilike(target)) |
                (ResidentModel.email.ilike(target)) |
                (ResidentModel.name.ilike(target))
            ).order_by(ResidentModel.created_at.desc()).paginate(page=page, per_page=per_page, error_out=False)

            for resident in resultset:
                residents.append(resident.to_JSON())

            return residents

        except Exception as ex:
            raise Exception( ex)
        
    @classmethod
    def add_resident(self, resident):

        try:
            db.session.add(resident)
            db.session.commit()

            return True
        except Exception as ex:
            print("valor de ex",ex)
            raise Exception( str(ex))
        

    @classmethod
    def update_resident(self, resident):
        try:
            resident_updated = ResidentModel.query.get(resident.id)

            resident_updated.name =  resident.name 
            resident_updated.last_name =  resident.last_name 
            resident_updated.phone =  resident.phone 
            resident_updated.email =  resident.email 
            resident_updated.age =  resident.age
            resident_updated.address =  resident.address
            resident_updated.delivered_food =  resident.delivered_food
            resident_updated.observation =  resident.observation

            db.session.commit()

            return True

        except Exception as ex:
            print("Error durante la actualización:", ex)
            db.session.rollback()
            raise Exception(str(ex))


    @classmethod
    def delete_resident(self, resident):
        try:
            resident_delete = ResidentModel.query.get(resident.id)
            db.session.delete(resident_delete)
            db.session.commit()
            return  True
        
        except Exception as ex:
            raise Exception( ex)
        

    @classmethod
    def filter_by_age_descending(self,  page, per_page ):
        try:
            residents =[]
            resultset = ResidentModel.query.order_by(text("age desc"), ResidentModel.created_at.desc()).paginate(page=page, per_page=per_page, error_out=False)
            for resident in resultset:
                residents.append(resident.to_JSON())
            return  residents
        
        except Exception as ex:
            raise Exception( ex)


    @classmethod
    def filter_by_name_ascending(self, page, per_page):
        try:
            residents = []
            resultset = ResidentModel.query.order_by(text("name asc"), ResidentModel.created_at.desc()).paginate(page=page, per_page=per_page, error_out=False)

            for resident in resultset:
                residents.append(resident.to_JSON())
                    
            return  residents
        
        except Exception as ex:
            raise Exception(ex)
        