import sqlite3

with sqlite3.connect('kuliah.db') as db:
    cur = db.cursor()

# hapus data kuliah
cur.execute("DELETE FROM Kuliah WHERE Kode_Dos = 'DL2';")

# hapus data Dosen
cur.execute("DELETE FROM Dosen WHERE Kode_Dos = 'DL2';")

# hapus data Mata Kuliah
cur.execute("DELETE FROM MataKuliah WHERE Kode_MK = 'MK3';")


db.commit()