
from fastapi.security import HTTPBearer
from fastapi import Request, HTTPException
from jwt_maneger import create_token, validate_token

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth= await super().__call__(request)
        data = validate_token(auth.credentials)
        if data['email'] != "vale@gmail.com":
            raise HTTPException(status_code=403, detail="credenciales invalidas") 