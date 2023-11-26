class  Response():
    
    @staticmethod
    def success_response(message,data=None):
        return {
            "status": "success",
            "message":  message,
            "data": data
        }
    
    @staticmethod
    def error_response(message,status_code, error_details=None):
        response = {
            "status": "error",
            "message": message,
        }
        if error_details:
            response["error_details"] = error_details
            response['code'] = status_code
        return response