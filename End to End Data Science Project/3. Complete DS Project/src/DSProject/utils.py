import os
import sys
import pandas as pd
from src.DSProject.logger import logging
from src.DSProject.exception import CustomException
from src.DSProject.utils import read_sql_data
from dotenv import load_dotenv
import pymysql

load_dotenv()
host = os.getenv("host"),
user = os.getenv("user"),
password = os.getenv("password"),
db = os.getenv("db")


def read_data_mysql():
    logging.info("Reading Data From MYSQL Started")
    try:
        mydb = pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )
        logging.info("Connection Established" , mydb)
        dataframe = pd.read_sql_query('select * from students', mydb)
        print(dataframe.head())

        return dataframe
    
    except Exception as e:
        raise CustomException()

    