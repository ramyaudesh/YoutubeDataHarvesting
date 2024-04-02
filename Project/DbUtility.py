import mysql.connector
import sqlalchemy 
from mysql.connector import Error
from mysql import connector
from Dataframe import *
    
def create_connection(host_name,user_name,user_password,db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        mousecursor=connection.cursor()
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection




    
    
