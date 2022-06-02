import sqlite3

with sqlite3.connect('toko.db') as db:
    cur = db.cursor()

#  data supplier
cur.execute("INSERT INTO Supplier VALUES ('1', 'LUFFY'), ('2', 'ZORO');")

#  data Nota
cur.execute("INSERT INTO Nota VALUES ('01' ,date('now'), '5 hari', 16000000, '1'), ('02',date('now'), '5 hari', 20000000, '2');")

#  barang
cur.execute(
    "INSERT INTO Barang VALUES ('L1', 'INFINIX'), ('L2', 'ROG');")

#  tr_brg
cur.execute(
    "INSERT INTO Tr_Brg VALUES ('01', 'L1', 2, 16000000), ('02', 'L2', 1, 20000000);")

db.commit()