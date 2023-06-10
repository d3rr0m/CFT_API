from sqlalchemy import create_engine, text, Connection
from fastapi import Depends
from session import get_db

DB_PATH = 'sqlite:///database.db'

class DAL:
    def __init__(self, db_session: Connection):
        self.db_session = db_session

def create_db(conn):

    create_query = '''
    create table if not exists employees(
    id integer primary key autoincrement,
    login text unique,
    salary real,
    increment_date date,
    password_hash text
    )'''
    insert_query = '''
    insert into employees 
    (login, salary, increment_date, password_hash) values
    ('Roman', 123.33, 08.06, '$2b$12$jYxDraYpMVasqX.zEkmxGO175YNTJyI8W.s1VhkazW6zGDw41en1a')
    '''
    #engine = create_engine(DB_PATH, echo=True)  
    #with engine.connect() as conn:
    conn.execute(text(create_query))
    conn.execute(text(insert_query))
            #conn.execute(text('insert into tablo values (1)'))
    conn.commit()

if __name__== '__main__':
    #db_conn = Depends(get_db)
    #print(get_db())
    #print (db_conn)
    create_db(conn= Depends(get_db))
