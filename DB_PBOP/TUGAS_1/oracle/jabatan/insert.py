import cx_Oracle

con = cx_Oracle.connect(
    "admin",
    "admin",
    "127.0.0.1/XE"
)

cur = con.cursor()

cur.execute("INSERT INTO jabatan VALUES('1','Presdir', 45000000, 20000000)")
cur.execute("INSERT INTO jabatan VALUES('2','Bendahara', 30000000, 15000000)")
cur.execute("INSERT INTO jabatan VALUES('3','Sekretaris', 29000000, 1500000)")

con.commit()
cur.close()
con.close()