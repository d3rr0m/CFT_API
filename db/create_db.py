@@ -1,30 +0,0 @@
from sqlalchemy import create_engine, text

DB_PATH = 'sqlite:///database.db'

def create_db():

    create_query = '''
    create table employees(
    id integer primary key autoincrement,
    name text,
    salary real,
    increment_date date,
    password_hash text
    )'''

    insert_query = '''
    insert into employees 
    (name, salary, increment_date, password_hash) values
    ('Roman', 123.33, 08.06, '$2b$12$jYxDraYpMVasqX.zEkmxGO175YNTJyI8W.s1VhkazW6zGDw41en1a')
    '''

    engine = create_engine(DB_PATH, echo=True)  
    with engine.connect() as conn:
        conn.execute(text(create_query))
        conn.execute(text(insert_query))
        #conn.execute(text('insert into tablo values (1)'))
        conn.commit()

if __name__== '__main__':
    create_db()