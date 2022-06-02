import cx_Oracle

con = cx_Oracle.connect(
    "admin",
    "admin",
    "127.0.0.1/XE"
)

cur = con.cursor()

cur.execute("SELECT * FROM pegawai")
result = cur.fetchall()

for row in result:
    print('%s,%s,%s,%s, %s, %.0f' % (row[0],row[1],row[2],row[3],row[4],row[5]))

print("------------------------")

cur.execute(''' UPDATE pegawai 
                 SET nama_pegawai = :1
                 WHERE kode_jabatan = :2''', ('Feri', 'P03'))

cur.execute("SELECT * FROM pegawai")
result = cur.fetchall()

for row in result:
    print('%s,%s,%s,%s, %s, %.0f' % (row[0],row[1],row[2],row[3],row[4],row[5]))

cur.close()
con.close()