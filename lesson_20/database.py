import pprint
import os

from dotenv import load_dotenv
import psycopg2

load_dotenv()


class PostgresDB:
    def __init__(self):
        self.dbname = os.getenv("dbname")
        self.user = os.getenv("user")
        self.password = os.getenv("password")
        self.host = os.getenv("host")
        self.port = os.getenv("port")
        self.__cursor = None
        self.__set_connection()

    def __set_connection(self):
        try:
            self.__connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            self.__connection.autocommit = True
            print("Connected to the database successfully!")
            self.__cursor = self.__connection.cursor()


        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)

    @property
    def cursor(self):
        return self.__cursor

    @property
    def connect(self):
        return self.__connection

    def query(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.__connection.close()


db_client = PostgresDB()

result = db_client.query(f"SELECT * FROM products")

pprint.pprint(result)
