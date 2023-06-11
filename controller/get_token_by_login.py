from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from sqlalchemy import create_engine, text

DB_PATH = 'sqlite:///database.db'
SECRET_KEY = '09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7'

def get_token_by_login(login: str, password: str)-> str:
   hashed_password = get_user_hashed_password(login)
   result = verify_password(password, hashed_password)
   return result
    
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(login: str, password :str):
    if verify_password():
        return pwd_context.genhash(SECRET_KEY,)

def get_password_hash(password: str):
    return pwd_context.hash(password)

def get_user_hashed_password(login: str) -> str:
    engine = create_engine(DB_PATH, echo=True)
    with engine.connect() as conn:
        query = f'select password_hash from employees where login = "{login}"'
        result = conn.execute(text(query))
    for row in result:
        return row[0]

if __name__ == '__main__':
    pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')
    #print(pwd_context.hash('pass'))
    get_token_by_login('Roman', 'pass')