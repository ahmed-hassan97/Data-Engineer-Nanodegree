import psycopg2
import argparse
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

DB_PASS = "root"
DB_USER = "postgres"
DB_HOST = "127.0.0.1"
PORT = 5432
dbname="PostGressModeling"

'''
    function to connect with database 
    return conn
'''
def connect_database(dpname):

    conn = psycopg2.connect(host = DB_HOST,user = DB_USER,password = DB_PASS , dbname = dpname)
    conn.set_session(autocommit = True)  
    cur = conn.cursor() 
   
    return conn , cur

def close_connection(cur , conn):
    cur.close()
    conn.close()
    return "connection is closed "

