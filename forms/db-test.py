import psycopg2
from members import g1
from def_config import db_config as dbc


class db:
    connection = psycopg2.connect(
        dbname=dbc.DB_NAME,
        user=dbc.DB_USER,
        password=dbc.DB_PASSWD,
        host=dbc.DB_HOST,
        port=dbc.DB_PORT
    )

    @classmethod
    def connect_cursor():
        global cursor = db.connection.cursor()

    def create_db_table(name, **kwargs):
        create_table_query = f'''
        CREATE TABLE IF NOT EXISTS {name} (
            name VARCHAR(16),
            logo VARCHAR(128),
            played_games INT,
            wins INT,
            id SERIAL PRIMARY KEY,
            members INT,
            invented DATE
        );
        '''
    cursor.execute(create_table_query)
    connection.commit()


insert_query = '''
INSERT INTO users (id ,name ,logo ,played_games ,wins ,members ,invented ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);
'''
data_to_insert = g1.return_datas()
cursor.execute(insert_query, data_to_insert)
connection.commit()
