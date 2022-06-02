import psycopg2

db = psycopg2.connect(
    user="postgres",
    password="ABEL",
    host="localhost",
    database="job"
)

cur = db.cursor()

# delete  gaji
cur.execute("DELETE FROM Gaji WHERE nip = '0013455' ;")

# delete pegawai
cur.execute("DELETE FROM Pegawai WHERE nip = '0013455' ;")

# delete golongan
cur.execute("DELETE FROM Golongan WHERE kode_golongan = '2' ;")

# delete jabatan
cur.execute("DELETE FROM jabatan WHERE kode_jabatan = 'A3' ;")

db.commit()