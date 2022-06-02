import cx_Oracle

con = cx_Oracle.connect(
    "admin",
    "admin",
    "127.0.0.1/XE"
)

cur = con.cursor()
sql = ''' 
      CREATE TABLE gaji( 
          bulan VARCHAR (20) NOT NULL PRIMARY KEY,
          nip VARCHAR (20),
          masuk NUMBER(5),
          sakit NUMBER(5),
          ijin NUMBER(5),
          alpha NUMBER(5),
          lembur NUMBER(5),
          potongan NUMBER(5)
      )
'''
cur.execute(sql)
cur.close()
con.close()