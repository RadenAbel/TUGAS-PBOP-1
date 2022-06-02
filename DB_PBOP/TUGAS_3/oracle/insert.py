import cx_Oracle

con = cx_Oracle.connect(
    "admin",
    "admin",
    "127.0.0.1/XE"
)

cur = con.cursor()

#  data supplier
cur.execute("INSERT INTO Supplier VALUES ('1', 'LUFFY')")
cur.execute("INSERT INTO Supplier VALUES ('2', 'ZORO')")

#  data Nota
cur.execute("INSERT INTO Nota VALUES ('01' ,DATE '2022-07-26', '5 hari', 16000000, '1')")
cur.execute("INSERT INTO Nota VALUES ('02',DATE '2022-07-26', '5 hari', 20000000, '2')")

#  barang
cur.execute("INSERT INTO Barang VALUES ('L1', 'INFINIX')")
cur.execute("INSERT INTO Barang VALUES ('L2', 'ROG')")

#  tr_brg
cur.execute("INSERT INTO Tr_Brg VALUES ('01', 'L1', 2, 16000000)")
cur.execute("INSERT INTO Tr_Brg VALUES ('02', 'L2', 1, 20000000)")

con.commit()