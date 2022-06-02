import cx_Oracle

con = cx_Oracle.connect(
    "admin",
    "admin",
    "127.0.0.1/XE"
)

cur = con.cursor()

cur.execute("INSERT INTO gaji VALUES('a','P01', 10, 1, 0, 0, 3, 20)")
cur.execute("INSERT INTO gaji VALUES('c','P02', 10, 0, 0, 2, 2, 50)")
cur.execute("INSERT INTO gaji VALUES('v','P03', 10, 1, 2, 0, 3, 30)")


con.commit()
cur.close()
con.close()