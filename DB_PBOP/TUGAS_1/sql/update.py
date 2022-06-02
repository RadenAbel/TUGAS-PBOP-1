import sqlite3

with sqlite3.connect('pegawai.db') as db:
    cur = db.cursor()

# update data gaji
cur.execute(
    "UPDATE Gaji SET masuk = 5, sakit = 0, ijin = 0, alpha = 0 WHERE nip = '0013455'")

# update pegawai
cur.execute(
    "UPDATE Pegawai SET nama_pegawai = 'RADEN ABEL' WHERE nip = '0023456'")


# update Golongans
cur.execute(
    "UPDATE Golongan SET tunjangan_suami = 50000000 WHERE kode_golongan = '2'")

# update jabatan
cur.execute(
    "UPDATE jabatan SET gapok = 30000000 WHERE kode_jabatan = 'A2'")

db.commit()