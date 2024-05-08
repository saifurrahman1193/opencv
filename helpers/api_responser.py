from fastapi.responses import JSONResponse
from fastapi import Request
# import logging

class ApiResponser:
    @staticmethod
    def set_response(data, status_code, status, message, request=None):
        res_data = {
            'status': status,
            'code': status_code,
            'data': data,
            'message': message
        }

        # logging.warning('================================================================================')
        response = JSONResponse(content=res_data, status_code=200, headers={'Content-Type': 'application/json'})

        return response
