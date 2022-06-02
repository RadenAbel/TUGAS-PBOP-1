import cx_Oracle

con = cx_Oracle.connect(
    "admin",
    "admin",
    "127.0.0.1/XE"
)

cur = con.cursor()

cur.execute("INSERT INTO pegawai VALUES('111','Raden', 'P01', '001', 'AKTIF', 0)")
cur.execute("INSERT INTO pegawai VALUES('112','Abel', 'P02', '002', 'AKTIF', 0)")
cur.execute("INSERT INTO pegawai VALUES('113','Danu', 'P03', '003', 'TIDAK AKTIF', 23)")


con.commit()
cur.close()
con.close()