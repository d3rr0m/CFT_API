from datetime import timedelta, datetime
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from sqlalchemy import create_engine, text
from jose import jwt

import settings

def get_token_by_login(login: str, expires_delta: timedelta)-> str:
   expire_date = str(datetime.utcnow() + timedelta(expires_delta))
   to_encode = dict(login=login, expire_date=expire_date)
   encoded = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
   return encoded
    
def verify_password(plain_password, hashed_password):
    pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
    return pwd_context.verify(plain_password, hashed_password)
