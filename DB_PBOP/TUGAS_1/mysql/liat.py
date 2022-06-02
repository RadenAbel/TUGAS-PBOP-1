import mysql.connector

db = mysql.connector.connect(
    user='root', 
    password='', 
    host='localhost', 
    database='job')
    
cur = db.cursor()

print("\n----- Data Table pegawai -----")
cur.execute("SELECT * FROM Pegawai")
result = cur.fetchall()
for row in result:
    print("%s, %s, %s, %s, %s, %s" %
          (row[0], row[1], row[2], row[3], row[4], row[5]))


# show data table jabatan
print("\n----- Data Table Jabatan -----")
cur.execute("SELECT * FROM jabatan")
result = cur.fetchall()
for row in result:
    print("%s, %s, %s, %s" %
          (row[0], row[1], row[2], row[3]))


# show data table golongan
print("\n----- Data Table Golongan -----")
cur.execute("SELECT * FROM Golongan")
result = cur.fetchall()
for row in result:
    print("%s, %s, %s, %s, %s, %s, %s" %
          (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

# show data table gaji
print("\n----- Data Table Gaji -----")
cur.execute("SELECT * FROM Gaji")
result = cur.fetchall()
for row in result:
    print("%s, %s, %s, %s, %s, %s, %s, %s" %
          (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
