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
        

def create_db(db):

    create_query = '''
    create table employees(
    id integer primary key autoincrement,
    login text unique,
    salary real,
    increment_date date,
    password_hash text
    )'''

    insert_query = '''
    insert into employees 
    (name, salary, increment_date, password_hash) values
    ('Roman', 123.33, 08.06, '$2b$12$jYxDraYpMVasqX.zEkmxGO175YNTJyI8W.s1VhkazW6zGDw41en1a')
    '''

    #engine = create_engine(DB_PATH, echo=True)  
    #with engine.connect() as conn:
    db.execute(text(create_query))
    db.execute(text(insert_query))
        #conn.execute(text('insert into tablo values (1)'))
    db.commit()        

if __name__== '__main__':
    db_conn = Depends(get_db)
    create_db(db_conn)        
