import cx_Oracle

con = cx_Oracle.connect(
    "admin",
    "admin",
    "127.0.0.1/XE"
)

cur = con.cursor()

# liat supplier
print("\n------- Data supplier --------")
cur.execute("SELECT * FROM Supplier")
for row in cur.fetchall():
    print("%s ,%s" % (row[0], row[1]))
# liat nota
print("\n\nData nota")
cur.execute("SELECT * FROM Nota")
for row in cur.fetchall():
    print("%s ,%s ,%s ,%s ,%s" % (row[0], row[1], row[2], row[3], row[4]))
# liat barang
print("\n-------- Data Barang --------")
cur.execute("SELECT * FROM barang")
for row in cur.fetchall():
    print("%s ,%s" % (row[0], row[1]))
# liat tr_brg
print("\n-------- Data Transaksi Barang ---------")
cur.execute("SELECT * FROM Tr_Brg")
for row in cur.fetchall():
    print("%s ,%s ,%s ,%s" % (row[0], row[1], row[2], row[3]))