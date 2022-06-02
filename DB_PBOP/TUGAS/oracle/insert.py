import cx_Oracle

db = cx_Oracle.connect(
    "admin",
    "admin",
    "127.0.0.1/XE"
)

cur = db.cursor()

cur.execute("INSERT INTO cabangbank VALUES ('SGT', 'SANGATTA', 'SANGATTA KALIMANTAN TIMUR')")
cur.execute("INSERT INTO cabangbank VALUES ('SMR', 'SAMARINDA', 'SAMARINDA KALIMANTAN TIMUR')")


cur.execute("INSERT INTO nasabah VALUES ('SGT1', 'Raden', 'Kec. KUTAI TIMUR')")
cur.execute("INSERT INTO nasabah VALUES ('SGT2', 'Gesya', 'Kec. KIRIGAKURE')")
cur.execute("INSERT INTO nasabah VALUES ('SMR1', 'Naruto', 'Kec. KONOHA')")


cur.execute("INSERT INTO rekening VALUES ('1', '11', 'SGT1', 'SGT', 45000000)")
cur.execute("INSERT INTO rekening VALUES ('2', '22', 'SGT2', 'SGT', 15000000)")
cur.execute("INSERT INTO rekening VALUES ('3', '33', 'SMR1', 'SMR', 5000000)")


cur.execute("INSERT INTO transaksi VALUES ('TR3' , 'VVIP', 'SMR1', date'2003-02-22', 60000000)")
cur.execute("INSERT INTO transaksi VALUES ('TR1' , 'PREMIUM', 'SGT1', date'2003-02-22', 8000000)")



db.commit()