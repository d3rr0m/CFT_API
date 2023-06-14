from sqlalchemy import create_engine, text, Connection

import settings

class DAL:
    def __init__(self, db_session: Connection):
        self.db_session = db_session

def create_db():

    create_employees_query = text(
    '''
    CREATE TABLE IF NOT EXISTS employees(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    login TEXT UNIQUE,
    salary REAL,
    increment_date TEXT,
    hashed_password TEXT);
    ''')
    
    #exmaple data - login: Roman, password: pass
    insert_employees_data_query = text(
    '''
    INSERT INTO employees 
    (login, salary, increment_date, hashed_password) VALUES
    ('Roman', 123.33, '2023-08-01', '$2b$12$jYxDraYpMVasqX.zEkmxGO175YNTJyI8W.s1VhkazW6zGDw41en1a')
    RETURNING id
    ''')

    engine = create_engine(settings.CREATE_DB_PATH, echo=True)  
    with engine.connect() as conn:
        conn.execute(create_employees_query)
        conn.execute(insert_employees_data_query).fetchone()
        conn.commit()

if __name__== '__main__':
    create_db()
