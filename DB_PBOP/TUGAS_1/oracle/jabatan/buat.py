import cx_Oracle

con = cx_Oracle.connect(
    "admin",
    "admin",
    "127.0.0.1/XE"
)

cur = con.cursor()
sql = ''' 
      CREATE TABLE jabatan ( 
          kode_jabatan VARCHAR (3) NOT NULL PRIMARY KEY,
          nama_jabatan VARCHAR (40),
          gapok INTEGER,
          tunjangan_jabatan INTEGER
      )
'''
cur.execute(sql)
cur.close()
con.close()