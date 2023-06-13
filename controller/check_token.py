#import jwt
from jose import jwt, JWTError 
from fastapi import HTTPException, status
from datetime import datetime

import settings

def check_is_valid_token(token: str)-> tuple:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
         payload = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
         expiration_date = datetime.strptime(payload['expiration_date'],'%Y-%m-%d %H:%M:%S.%f')
         is_valid = expiration_date > datetime.utcnow()
         return (payload['login'], payload['expiration_date'], is_valid)
    except JWTError:
         raise credentials_exception
    