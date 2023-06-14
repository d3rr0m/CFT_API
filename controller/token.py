from datetime import timedelta, datetime
from passlib.context import CryptContext
from jose import jwt

import settings

def get_token_by_login(login: str, expires_delta: timedelta)-> str:
   expiration_date = str(datetime.utcnow() + timedelta(minutes=expires_delta))
   to_encode = dict(login=login, expiration_date=expiration_date)
   token = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
   return token
    
def verify_password(plain_password, hashed_password):
    pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
    return pwd_context.verify(plain_password, hashed_password)
