from cassandra.cluster import Cluster

"""

    Function to Connect With Cassandra
    input  : None
    output : session 

"""
def connectCassandra():
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()
    
    return session
