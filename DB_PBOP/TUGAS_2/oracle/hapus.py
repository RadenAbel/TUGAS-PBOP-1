import cx_Oracle

con = cx_Oracle.connect(
    "admin",
    "admin",
    "127.0.0.1/XE"
)
cur = con.cursor()

# hapus data kuliah
cur.execute("DELETE FROM Kuliah WHERE Kode_Dos = 'DL2'")

# hapus data Dosen
cur.execute("DELETE FROM Dosen WHERE Kode_Dos = 'DL2'")

# hapus data Mata Kuliah
cur.execute("DELETE FROM MataKuliah WHERE Kode_MK = 'MK3'")


