from django.shortcuts import render

from django.http import HttpResponse
import psycopg2
import logging

def index(request):
    import os
    postgrepw = os.getenv('postgrepw')

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

    def fetch_all(self):
        try:
            conn = get_connection('spd')
            if conn:
                logging.debug('Database connection established')
                curr = conn.cursor()

                curr.execute("SELECT * FROM spd")
                data = curr.fetchall()

                # for row in data:
                #     print(row)
                conn.close()
            else:
                logging.error('Database connection failed')
        except:
            logging.error('Error getting results from table')
    return data
    #return HttpResponse("Hello, world. You're at the Seattle index.")
