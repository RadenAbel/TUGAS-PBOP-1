import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="kuliah"
)

cur = db.cursor()

#  data Dosen
print("Tampilkan data Dosen")
cur.execute("SELECT * FROM Dosen")
result = cur.fetchall()
for row in result:
    print("%s ,%s ,%s ,%s" % (row[0], row[1], row[2], row[3]))

#  data Kuliah
print("\n\nTampilkan data Kuliah")
cur.execute("SELECT * FROM Kuliah")
result = cur.fetchall()
for row in result:
    print("%s ,%s ,%s ,%s" % (row[0], row[1], row[2], row[3]))

#  data MataKuliah
print("\n\nTampilkan data Mata Kuliah")
cur.execute("SELECT * FROM MataKuliah")
result = cur.fetchall()
for row in result:
    print("%s ,%s ,%s ,%s" % (row[0], row[1], row[2], row[3]))