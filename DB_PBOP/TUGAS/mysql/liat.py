import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='atm'
)
cur = db.cursor()

print("\n----- Data CabangBank")
cur.execute("SELECT * FROM cabangbank")
for row in cur.fetchall():
    print("%s ,%s ,%s" % (row[0], row[1], row[2]))

print("\n------ Data Nasabah -----")
cur.execute("SELECT * FROM nasabah")
for row in cur.fetchall():
    print("%s ,%s ,%s" % (row[0], row[1], row[2]))

print("\n------ Data Rekening --------")
cur.execute("SELECT * FROM rekening")
for row in cur.fetchall():
    print("%s ,%s ,%s ,%s ,%s" % (row[0], row[1], row[2], row[3], row[4]))

print("\n------ Data Transaksi ------")
cur.execute("SELECT * FROM transaksi")
for row in cur.fetchall():
    print("%s ,%s ,%s ,%s ,%s" % (row[0], row[1], row[2], row[3], row[4]))