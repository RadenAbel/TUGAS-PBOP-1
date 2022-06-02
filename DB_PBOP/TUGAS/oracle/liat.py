import cx_Oracle

db = cx_Oracle.connect(
    "admin",
    "admin",
    "127.0.0.1/XE"
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