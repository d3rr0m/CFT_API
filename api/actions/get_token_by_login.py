from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext

SECRET_KEY = '09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7'
def get_token_by_login(login: str, password: str)-> str:
    if password:
        return login
    
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(login: str, password :str):
    if verify_password:
        return pwd_context.genhash(SECRET_KEY,)
    
if __name__ == '__main__':
    pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')
    print(pwd_context.hash('pass', scheme='bcrypt'))