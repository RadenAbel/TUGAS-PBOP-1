import cx_Oracle

con = cx_Oracle.connect(
    "admin",
    "admin",
    "127.0.0.1/XE"
)

cur = con.cursor()

cur.execute("SELECT * FROM gaji")
result = cur.fetchall()

for row in result:
    print('%s,%s,%.0f,%.0f,%.0f,%.0f,%.0f,%.0f' % (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]))

print("----------------")
cur.execute(''' DELETE FROM gaji WHERE nip = :1''', ('P02',))

cur.execute("SELECT * FROM gaji")
result = cur.fetchall()

for row in result:
    print('%s,%s,%.0f,%.0f,%.0f,%.0f,%.0f,%.0f' % (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]))
    
cur.close()
con.close()