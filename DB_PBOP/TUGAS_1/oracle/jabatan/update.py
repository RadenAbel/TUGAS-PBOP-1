import cx_Oracle

con = cx_Oracle.connect(
    "admin",
    "admin",
    "127.0.0.1/XE"
)

cur = con.cursor()

cur.execute("SELECT * FROM jabatan")
result = cur.fetchall()

for row in result:
    print('%s,%s,%.0f' % (row[0],row[1],row[2]))

print("--------------------------")

cur.execute(''' UPDATE jabatan 
                 SET nama_jabatan = :1
                 WHERE kode_jabatan = :2''', ('OB', '2'))

con.commit()
cur.execute("SELECT * FROM jabatan")
result = cur.fetchall()

for row in result:
    print('%s,%s,%.0f' % (row[0],row[1],row[2]))

cur.close()
con.close()