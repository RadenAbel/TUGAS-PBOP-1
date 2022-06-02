import cx_Oracle

con = cx_Oracle.connect(
    "admin",
    "admin",
    "127.0.0.1/XE"
)

cur = con.cursor()

cur.execute("SELECT * FROM golongan")
result = cur.fetchall()

for row in result:
    print('%s,%s,%.0f,%.0f,%.0f,%.0f,%.0f' % (row[0],row[1],row[2],row[3],row[4],row[5],row[6]))

print("------------------")
cur.execute(''' UPDATE golongan 
                 SET nama_golongan = :1
                 WHERE kode_golongan = :2''', ('Menikah', 'A1'))

cur.execute("SELECT * FROM golongan")
result = cur.fetchall()

for row in result:
    print('%s,%s,%.0f,%.0f,%.0f,%.0f,%.0f' % (row[0],row[1],row[2],row[3],row[4],row[5],row[6]))



cur.close()
con.close()