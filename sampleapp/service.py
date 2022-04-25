from lib2to3.pgen2 import token
from rest_framework_jwt.settings import api_settings


def generatetoken(user):
    jwt_payload_handler=api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler=api_settings.JWT_ENCODE_HANDLER
    payload=jwt_payload_handler(user)
    token=jwt_encode_handler(payload)
    return {"token":token}


# to generate the token:
    
    
#     1.given the settings in payload handler---
#     api_settings




