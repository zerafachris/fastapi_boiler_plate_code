import jwt
from jwt.exceptions import InvalidTokenError
from fastapi import FastAPI, Depends, HTTPException,status
from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from models import TokenTable

ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 30 minutes
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7 # 7 days
ALGORITHM = "HS256"
JWT_SECRET_KEY = "narsimha"   # should be kept secret
JWT_REFRESH_SECRET_KEY = "134narsimha"

def decodeJWT(jwtoken: str):
    try:
        # Decode and verify the token
        payload = jwt.decode(jwtoken, JWT_SECRET_KEY, ALGORITHM)
        return payload
    except InvalidTokenError:
        return None


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=403, detail="Invalid token or expired token.")
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

    def verify_jwt(self, jwtoken: str) -> bool:
        isTokenValid: bool = False

        try:
            payload = decodeJWT(jwtoken)
        except:
            payload = None
        if payload:
            isTokenValid = True
        return isTokenValid

jwt_bearer = JWTBearer()

 

 
            







# import pymongo
# from rest_framework.exceptions import AuthenticationFailed
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["online_goods_delevery_db"]
# tokens = mydb['tokens']
# agent_tokens = mydb['agent_tokens']

# def token_required(func):
#     def inner(request, *args, **kwargs):
      
#         auth_header = request.headers.get('Authorization')
#         a_token = auth_header.split()[1]
#         details = tokens.find_one({"user_id":str(request.user._id),"access_token":a_token,"active":True})
#         if details:
#             return func(request, *args, **kwargs)
#         else:
#             raise AuthenticationFailed({'Message':'Token is blacklisted'})
         
#     return inner