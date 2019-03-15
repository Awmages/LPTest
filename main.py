import mysql.connector
import matplotlib.pyplot as plt

# Config settings for MySQL Connector
config = {
    "user": "root",
    "password": "lptech",
    "host": "127.0.0.1",
    "database": "test",
    "raise_on_warnings": True
}

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()


# Function to convert Hex to signed int
def twos_comp(val):
    comp_eval = int(val, 16) - pow(2, 32)
    comp_eval = int(hex(comp_eval), 16)
    return comp_eval


def main():

    query = ("SELECT * FROM test")
    cursor.execute(query)

    # Creates X axis, change cen_freq and span to match analyzers settings
    trace_array = []
    cen_freq = 1000
    span = 1000
    hal_span = float(span / 2)
    inc_span = float("{0:.2f}".format(span / 601))
    freq_star = cen_freq - hal_span
    for i in range(601):
        trace_array.append(freq_star + i * inc_span)

    # For loop to pull blob, convert to dBm, and then graph
    for entry in cursor:
        blob_array = []
        blob = entry[1].hex()
        for i in range(0, len(blob), 8):
            two_eval = twos_comp(blob[i:i+8])
            blob_array.append(two_eval/1000)

        # Styling for plot
        plt.style.use("dark_background")
        plt.plot(trace_array, blob_array, 'y', linewidth=1)
        plt.xlabel("MHz")
        plt.xlim(cen_freq-hal_span, cen_freq+hal_span)
        plt.ylabel("dBm")
        plt.ylim(-60, -30)
        plt.grid(color="gray", linestyle="-", linewidth=0.5)
        plt.text(cen_freq - 85 * inc_span, -59.1, entry[2])
        plt.text(cen_freq + 185 * inc_span, -33, "LPT Example", color="yellow")
        plt.draw()
        # Time replay speed
        plt.pause(1)
        plt.clf()


if __name__ == "__main__":
    while True:
        main()