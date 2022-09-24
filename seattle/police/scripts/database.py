import psycopg2
import logging
logging.basicConfig(level=logging.DEBUG)

import pandas as pd
from sqlalchemy import create_engine

import os
postgrepw = os.getenv('postgrepw')



class DatabaseInterface():


    def __init__(self, db):
        pass

    def get_connection(self):
        try:
            return psycopg2.connect(
                database="spd",
                user="postgres",
                password=postgrepw,
                host="127.0.0.1",
                port=5432,
            )

        except:
            return False

    # if conn:
    #     print("Connection to the PostgreSQL established successfully.")
    # else:
    #     print("Connection to the PostgreSQL encountered and error.")

    def fetch_all(self):
        try:
            conn = DatabaseInterface.get_connection('spd')
            if conn:
                logging.debug('Database connection established')
                curr = conn.cursor()

                curr.execute("SELECT * FROM spd")
                data = curr.fetchall()
                for row in data:
                     print(row)
                conn.close()
            else:
                logging.error('Database connection failed')
        except:
            logging.error('Error getting results from table')

