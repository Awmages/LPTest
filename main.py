import mysql.connector
import matplotlib.pyplot as plt

# Config file for MySQL Connector
config = {
    'user': 'root',
    'password': 'lptech',
    'host': '127.0.0.1',
    'database': 'test',
    'raise_on_warnings': True
}


def twos_comp (val):
    comp_eval = int(val, 16) - pow(2, 32)
    comp_eval = int(hex(comp_eval), 16)
    return comp_eval


cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

query = ("SELECT trace_data FROM test")

cursor.execute(query)

for entry in cursor:
    blob_array = []
    blob = entry[0].hex()
    


cnx.close()

