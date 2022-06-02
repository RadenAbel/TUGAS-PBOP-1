import cx_Oracle

con = cx_Oracle.connect(
    "admin",
    "admin",
    "127.0.0.1/XE"
)

cur = con.cursor()

cur.execute("INSERT INTO golongan VALUES('A1', 'Sendiri', 0, 0, 500000, 1000000, 500000)")
cur.execute("INSERT INTO golongan VALUES('A2', 'Menikah', 1500000, 1500000, 500000, 1000000, 800000)")
cur.execute("INSERT INTO golongan VALUES('A3', 'Sendiri', 0, 0, 800000, 1000000, 500000)")



con.commit()
cur.close()
con.close()