import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="kuliah"
)

cur = db.cursor()

cur.execute("INSERT INTO Dosen VALUES ('DL2', 'ESA AGE', 'KONOHA', '222222');")
cur.execute("INSERT INTO Dosen VALUES ('DL3', 'NARUTO', 'KONOHA', '333333');")

# insert data matakuliah
cur.execute("INSERT INTO MataKuliah VALUES ('MK1', 'PBOP', '1', '4');")
cur.execute("INSERT INTO MataKuliah VALUES ('MK2', 'ENGGLISH', '2', '2');")
cur.execute("INSERT INTO MataKuliah VALUES ('MK3', 'KEWARGANEGARAAN', '3', '3');")

# insert data Kuliah
cur.execute("INSERT INTO Kuliah VALUES ('MK1', 'DL2', '10:40', 'LK3.2');")
cur.execute("INSERT INTO Kuliah VALUES ('MK2', 'DL3', '14:40', 'D2.2');")
cur.execute("INSERT INTO Kuliah VALUES ('MK3', 'DL2', '08:00', 'D1.1');")

db.commit()