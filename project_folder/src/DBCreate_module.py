import psycopg2
import requests


class DBCreating:

    def __init__(self):
        self.__host = 'localhost'
        self.__databases = 'postgres'
        self.__username = 'postgres'
        self.__port = '5432'
        self.__password = 'nokwyz-2tigtY-pofjef'

    def db_creating(self, table_name):
        conn = psycopg2.connect(
            host=self.__host,
            databases=self.__databases,
            user=self.__username,
            port=self.__port,
            password=self.__password
        )
        cur = conn.cursor()
        cur.execute(f"CREATE TABLE {table_name} ()")

