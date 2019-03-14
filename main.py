import mysql.connector
import matplotlib.pyplot as plt

# Config file for MySQL Connector
config = {
    "user": "root",
    "password": "lptech",
    "host": "127.0.0.1",
    "database": "test",
    "raise_on_warnings": True
}

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

def twos_comp (val):
    comp_eval = int(val, 16) - pow(2, 32)
    comp_eval = int(hex(comp_eval), 16)
    return comp_eval


def main():

    query = ("SELECT * FROM test")
    cursor.execute(query)
           

    for entry in cursor:
        blob_array = []
        blob = entry[1].hex()
        for i in range(0, len(blob), 8):
            two_eval = twos_comp(blob[i:i+8])
            blob_array.append(two_eval/1000)

        plt.style.use("dark_background")
        plt.plot(blob_array, 'y', linewidth=1)
        plt.xlabel("MHz")
        plt.xlim(100, 500)
        plt.ylabel("dBm")
        plt.ylim(-60, -30)
        plt.grid(color="gray", linestyle="-", linewidth=0.5)
        plt.text(250, -59.1, entry[2])
        plt.text(425, -33, "LPT Example", color="yellow")
        plt.draw()
        plt.pause(.1)
        plt.clf()


if __name__ == "__main__":
    while True:
        main()
    cnx.close()