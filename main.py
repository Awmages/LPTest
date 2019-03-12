import mysql.connector

# Config file for MySQL Connector
config = {
    'user': 'root',
    'password': 'lptech',
    'host': '127.0.0.1',
    'database': 'test',
    'raise_on_warnings': True
}

cnx =mysql.connector.connect(**config)




