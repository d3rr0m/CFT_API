from typing import Generator
from sqlalchemy import create_engine, text, Connection
from fastapi import Depends

DB_PATH = 'sqlite:///database.db'
engine = create_engine(DB_PATH, echo=True)  
#conn = engine.connect()

def get_db() -> Generator:
    try:
        connection = engine.connect()
        yield connection
    finally:
        connection.close()
