import cx_Oracle

con = cx_Oracle.connect(
    "admin",
    "admin",
    "127.0.0.1/XE"
)

cur = con.cursor()
sql = ''' 
      CREATE TABLE pegawai ( 
          nip VARCHAR(20) NOT NULL PRIMARY KEY,
          nama_pegawai VARCHAR(40),
          kode_jabatan VARCHAR(3),
          kode_golongan VARCHAR(3),
          status VARCHAR (15),
          jumlah_anak INTEGER
      )
'''
cur.execute(sql)
cur.close()
con.close()