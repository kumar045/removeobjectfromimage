import ibm_db
import os
import re
import glob
# import json 
from flask import Flask
from flask import request
from flask import jsonify 
import json
import pandas as pd
app = Flask(__name__) 
dsn_hostname = os.environ['HOST_URL']
dsn_uid = os.environ['USERNAME']
dsn_pwd = os.environ['PASSWORD']
dsn_port = os.environ['PORT']
dsn_database = "bludb"            
dsn_driver = "{IBM DB2 ODBC DRIVER}"
dsn_protocol = "TCPIP"            
dsn_security = "SSL"              
#Create the dsn connection string
dsn = (
    "DRIVER={0};"
    "DATABASE={1};"
    "HOSTNAME={2};"
    "PORT={3};"
    "PROTOCOL={4};"
    "UID={5};"
    "PWD={6};"
    "SECURITY={7};").format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd, dsn_security)
# #Create database connection
try:
    conn = ibm_db.connect(dsn, "", "")
    print ("Connected to database: ", dsn_database, "as user: ", dsn_uid, "on host: ", dsn_hostname)
    command = "select * from cb106 where LOWER(NAME) like '%{}%' OR LOWER(DESCRIPTION) like '%{}%' ".format("arg","arg") 
except:
    print ("Unable to connect: ", ibm_db.conn_errormsg() )
# # Create the cb106 table
create = 'CREATE TABLE cb106 (courseType VARCHAR(20000), description VARCHAR(20000), id VARCHAR(20000), slug VARCHAR(20000), instructorIds VARCHAR(20000), specializations VARCHAR(20000), partnerIds VARCHAR(20000), name VARCHAR(20000))'
result = ibm_db.exec_immediate(conn, create)
# Populate the cb106 table
for csv_file in glob.glob("csv_files/*.csv"):

    data=pd.read_csv(csv_file)
    data=data.iloc[:,:].values
    res = tuple(map(tuple, data))

    insert = 'INSERT INTO cb106 (courseType, description, id, slug, instructorIds, specializations, partnerIds, name ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)'
    stmt = ibm_db.prepare(conn, insert)
    if stmt:
        for i in res:
            print(i)
        
            result = ibm_db.execute(stmt,i)

