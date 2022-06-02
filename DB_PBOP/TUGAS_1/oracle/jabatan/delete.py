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

cur.execute(''' DELETE FROM jabatan WHERE nama_jabatan = :1''', ('presdir',))
cur.execute("SELECT * FROM jabatan")
result = cur.fetchall()

for row in result:
    print('%s,%s,%.0f' % (row[0],row[1],row[2]))

cur.close()
con.close()