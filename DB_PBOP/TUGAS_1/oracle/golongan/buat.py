import cx_Oracle

con = cx_Oracle.connect(
    "admin",
    "admin",
    "127.0.0.1/XE"
)

cur = con.cursor()
sql = ''' 
      CREATE TABLE golongan( 
          kode_golongan VARCHAR (3) NOT NULL PRIMARY KEY,
          nama_golongan VARCHAR (10),
          tunjangan_suami NUMBER(10),
          tunjangan_anak NUMBER(10),
          uang_makan NUMBER(10),
          uang_lembur NUMBER(10),
          askes NUMBER(10)
      )
'''
cur.execute(sql)
cur.close()
con.close()