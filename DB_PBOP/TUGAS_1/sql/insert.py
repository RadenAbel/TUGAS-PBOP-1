import sqlite3

with sqlite3.connect('pegawai.db') as db:
    cur = db.cursor()

#  DATA JABATAN
cur.execute("INSERT INTO `jabatan` VALUES ('A1', 'PRESDIR', 20000000, 7000000)")
cur.execute("INSERT INTO `jabatan` VALUES ('A2', 'BENDAHARA', 3000000, 2000000)")
cur.execute("INSERT INTO `jabatan` VALUES ('A3', 'SEKRETARISS', 9000000, 4000000)")


#  DATA GOLONGAN
cur.execute("INSERT INTO `Golongan` VALUES ('1', 'SENDIRI', 3500000, 0, 100000, 200000, 100000)")
cur.execute("INSERT INTO `Golongan` VALUES ('2', 'MENIKAH', 500000, 500000, 1500000, 100000, 200000)")

#  DATA PEGAWAI
cur.execute("INSERT INTO `Pegawai` VALUES ('0013455', 'ESA AGE', 'A1' , '01', 'SENDIRI', 0)")
cur.execute("INSERT INTO `Pegawai` VALUES ('0023456', 'FERI', 'A2' , '02', 'SUDAH MENIKAH', 2)")


#  DATA GAJI
cur.execute("INSERT INTO `Gaji` VALUES ('JANUARI', '0013455', 15, 0, 0, 1, 0, 20000)")
cur.execute("INSERT INTO `Gaji` VALUES ('JANUARI', '0023456', 15, 2, 1, 0, 0, 80000)")


db.commit()