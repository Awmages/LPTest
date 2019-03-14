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
    for i in range(0, len(blob), 8):
        two_eval = twos_comp(blob[i:i+8])
        blob_array.append(two_eval/1000)
    plt.plot(blob_array)
    plt.draw()
    plt.pause(.1)
    plt.clf()


cnx.close()

