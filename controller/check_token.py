#import jwt
from jose import jwt, JWTError 
from fastapi import HTTPException, status

import settings

def check_is_valid_token(token: str)-> tuple:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
         payload = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
         return (payload['login'], payload['expire_date'])
    except JWTError:
         raise credentials_exception