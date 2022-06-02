import sqlite3

with sqlite3.connect('toko.db') as db:
    cur = db.cursor()

# liat supplier
print("\n------- Data Supplier --------")
cur.execute("SELECT * FROM Supplier;")
for row in cur.fetchall():
    print("%s ,%s" % (row[0], row[1]))

# liat nota
print("\n\nData Nota")
cur.execute("SELECT * FROM Nota;")
for row in cur.fetchall():
    print("%s ,%s ,%s ,%s ,%s" % (row[0], row[1], row[2], row[3], row[4]))

# liat barang
print("\n-------- Data Barang --------")
cur.execute("SELECT * FROM Barang;")
for row in cur.fetchall():
    print("%s ,%s" % (row[0], row[1]))

# liat tr_brg
print("\n-------- Data Transaksi Barang ---------")
cur.execute("SELECT * FROM Tr_Brg;")
for row in cur.fetchall():
    print("%s ,%s ,%s ,%s" % (row[0], row[1], row[2], row[3]))