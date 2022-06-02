import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="kuliah"
)

cur = db.cursor()



# update data Dosen
cur.execute("UPDATE Dosen SET Nama_Dos = 'SASUKE' WHERE Kode_Dos = 'DL2';")

# update data Kuliah
cur.execute(
    "UPDATE Kuliah SET Tempat = 'D2.2' WHERE Kode_MK = 'MK2';")

# update data mata kuliah
cur.execute(
    "UPDATE MataKuliah SET Nama_MK = 'AAP' WHERE Kode_MK = 'MK3';")

db.commit()