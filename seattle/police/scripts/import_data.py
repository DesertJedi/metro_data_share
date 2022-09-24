import logging
logging.basicConfig(level=logging.DEBUG)
import database
import os
from sqlalchemy import create_engine

def import_csv(file):

    # Instantiate sqlachemy.create_engine object
    postgrepw = os.getenv('postgrepw')
    engine = create_engine('postgresql://postgres:'+postgrepw+'@localhost:5432/spd')

    import psycopg2 as pg

    # c = conn.cursor()
    # c.execute('''DROP TABLE IF EXISTS spd''')
    # c.execute('''CREATE TABLE IF NOT EXISTS spd (id varchar, incident_num int, incident_type text, occured_date_time text, precinct text, sector text, beat text, officer_id int, subject_id int, subject_race text, subject_gender text)''')

    import pandas as pd
    import pandas.io.sql as psql
    # load the data into a Pandas DataFrame
    data = pd.read_csv(file)
    # write the data to a sqlite table
    data.to_sql('spd', engine, if_exists='replace', index = False)

if __name__ == '__main__':


    # Import CSV file into new postgre table
    file= r'..\csv_data\Use_Of_Force.csv'
    import_csv(file)

    # Test function
    db = 'spd'
    data = database.DatabaseInterface(db)
    print(data.fetch_all())
