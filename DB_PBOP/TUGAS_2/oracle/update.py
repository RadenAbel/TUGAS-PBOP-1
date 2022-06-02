import cx_Oracle

con = cx_Oracle.connect(
    "admin",
    "admin",
    "127.0.0.1/XE"
)
cur = con.cursor()

# update data Dosen
cur.execute("UPDATE Dosen SET Nama_Dos = 'SASUKE' WHERE Kode_Dos = 'DL2'")

# update data Kuliah
cur.execute(
    "UPDATE Kuliah SET Tempat = 'D2.2' WHERE Kode_MK = 'MK2'")

# update data mata kuliah
cur.execute(
    "UPDATE MataKuliah SET Nama_MK = 'AAP' WHERE Kode_MK = 'MK3'")

con.commit()
cur.close()
con.close()