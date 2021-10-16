import psycopg2
from sql_queries import create_table_queries, drop_table_queries
from connect import *

def create_database():
    """
    Creates the Database to insert the data
    :return: cursor an connection
    """
    # connect to default database
    conn , cur = connect_database("PostGressModeling")
    conn.set_session(autocommit=True)
    print("connect to postgress database ")
    # create sparkify database with UTF8 encoding
    # cur.execute("DROP DATABASE IF EXISTS Sparkifydb")
    # cur.execute("CREATE DATABASE Sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")
    print("create sparkifydb")
    # close connection to default database
    conn.close()    
    
    # connect to sparkify database
    conn , cur = connect_database("sparkifydb")        
    return cur, conn


def drop_tables(cur, conn):
    """
    Drop all the tables.
    :param cur: cursor.
    :param conn: connection.
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    Create all the tables.
    :param cur: cursor.
    :param conn: connection.
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    cur, conn = create_database()
    
    drop_tables(cur, conn)
    create_tables(cur, conn)

    close_connection(cur , conn)


if __name__ == "__main__":
    main()