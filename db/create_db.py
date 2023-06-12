from sqlalchemy import create_engine, text, Connection

import settings

class DAL:
    def __init__(self, db_session: Connection):
        self.db_session = db_session

def create_db():

    create_query = '''
    create table if not exists employees(
    id integer primary key autoincrement,
    login text unique,
    salary real,
    increment_date date,
    hashed_password text
    )'''
    insert_query = '''
    insert into employees 
    (login, salary, increment_date, hashed_password) values
    ('Roman', 123.33, 08.06, '$2b$12$jYxDraYpMVasqX.zEkmxGO175YNTJyI8W.s1VhkazW6zGDw41en1a')
    '''
    engine = create_engine(settings.DB_PATH, echo=True)  
    with engine.connect() as conn:
        conn.execute(text(create_query))
        conn.execute(text(insert_query))
        conn.commit()

if __name__== '__main__':
    create_db()
