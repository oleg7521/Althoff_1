import csv

with open("st.csv", "r", encoding="utf8") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row))

