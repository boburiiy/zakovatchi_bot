import psycopg2
from functools import wraps


def handle_db_errors(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except psycopg2.Error as e:
            print(f"Database error in {func.__name__}: {e}")
            return None


class Database:
    def __init__(self, dbname, user, password, host, port):
        try:
            self.connection = psycopg2.connect(
                dbname=dbname,
                user=user,
                password=password,
                host=host,
                port=port
            )
            self.cursor = self.connection.cursor()
        except psycopg2.DatabaseError as err:
            print("db errror:", err)

    @handle_db_errors
    def execute(self, command: str):
        self.cursor.execute(command)

    @handle_db_errors
    def create_table(self, table_name: str, condition: str, **kwargs: dict) -> str:
        command = ''.join(f'{i} {j},\n' for i, j in kwargs.items())
        create_table_query = f'''
        {condition} {table_name} (
            {command.rstrip(',\n')}
        );
        '''
        return command

    @handle_db_errors
    def insert_data(self, table_name: str, vars: str, values: tuple) -> str:
        command = "INSERT INTO {table_name} {vars} VALUES {values}"
        return command

    @handle_db_errors
    def fetch_data(self, vars: str, table: str, condition=None, f1=False, fall=True, fmany=False, fmany_size=5) -> str:
        command = f"SELECT {vars} FROM {table} {
            condition if condition else ''}"
        self.execute(command)
        output = self.cursor.fetchone() if f1 else self.cursor.fetchmany(
            fmany_size) if fmany else self.cursor.fetchall()
        return output

    @handle_db_errors
    def commit(self):
        self.connection.commit()

    @handle_db_errors
    def close(self):

        self.cursor.close()
        self.connection.close()