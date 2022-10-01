#importing everything

import mysql.connector 
from mysql.connector import Error

def create_server_connection(host_name, username, user_password):
  connection = None
  try:
    connection = mysql.connector.connect(
      host = host_name,
      user = username,
      password = user_password)
  except Error as err:
    print(f"Error: '{err}'")
  return connection 

#Put mysql terminal password
pw = "1223gY15"

#Database name
db = "bnls1"
connection = create_server_connection("localhost", "root", pw)


# create mysql python 

"""def create_database(connection, query):
  cursor = connection.cursor()
  try:
    cursor.execute(query)
    print("database created successfully")
  except Error as err:
    print(f"Error: '{err}'")

create_database_query = "Create database bnls1"
create_database(connection, create_database_query)

#connect to database"""

def create_db_connection(host_name, username, user_password, db_name):
  connection = None
  try:
    connection = mysql.connector.connect(
    host = host_name,
    user = username,
    password = user_password,
    database = db_name)
    print("My sql db connection established")
  except Error as err:
     print(f"Error: '{err}'")
  return connection

#execute sql queries

def execute_query(connection, query):
  cursor = connection.cursor()
  try:
    cursor.execute(query)
    connection.commit()
    print("Query successfully executed")
  except Error as err:
    print(f"Error: '{err}'")
  

create_orders_table = """
CREATE TABLE mytable(
   id                      INTEGER  NOT NULL PRIMARY KEY 
  ,parking_id              VARCHAR(11) NOT NULL
  ,nom                     VARCHAR(57) NOT NULL
  ,insee                   INTEGER  NOT NULL
  ,adresse                 VARCHAR(92)
  ,url                     VARCHAR(163)
  ,type_usagers            VARCHAR(7) NOT NULL
  ,gratuit                 BIT  NOT NULL
  ,nb_places               INTEGER  NOT NULL
  ,nb_pr                   INTEGER 
  ,nb_pmr                  INTEGER 
  ,nb_voitures_electriques INTEGER 
  ,nb_velo                 INTEGER 
  ,nb_2r_el                INTEGER 
  ,nb_autopartage          INTEGER 
  ,nb_2_rm                 INTEGER 
  ,nb_covoit               INTEGER 
  ,hauteur_max             VARCHAR(3) NOT NULL
  ,num_siret               INTEGER  NOT NULL
  ,Xlong                   VARCHAR(17) NOT NULL
  ,Ylat                    VARCHAR(18) NOT NULL
  ,tarif_pmr               VARCHAR(13)
  ,tarif_1h                NUMERIC(5,2)
  ,tarif_2h                NUMERIC(5,2)
  ,tarif_3h                NUMERIC(5,2)
  ,tarif_4h                NUMERIC(5,2)
  ,tarif_24h               NUMERIC(6,2)
  ,abo_resident            NUMERIC(6,3)
  ,abo_non_resident        NUMERIC(6,3)
  ,type_ouvrage            VARCHAR(17)
  ,info                    VARCHAR(454)
  ,id_source               VARCHAR(11)
);
"""
  
#connect to the database
connection = create_db_connection("localhost","root", pw, db)
execute_query(connection, create_orders_table)