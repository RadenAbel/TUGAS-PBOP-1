import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='atm'
)
cur = db.cursor()


cur.execute("INSERT INTO cabangbank VALUES ('SGT', 'SANGATTA', 'SANGATTA KALIMANTAN TIMUR') , ('SMR', 'SAMARINDA', 'SAMARINDA KALIMANTAN TIMUR');")


cur.execute("INSERT INTO nasabah VALUES ('SGT1', 'Raden', 'Kec. KUTAI TIMUR'),  ('SGT2', 'Gesya', 'Kec. KIRIGAKURE'), ('SMR1', 'Naruto', 'Kec. KONOHA');")


cur.execute("INSERT INTO rekening VALUES ('1', '11', 'SGT1', 'SGT', 45000000), ('2', '22', 'SGT2', 'SGT', 15000000), ('3', '33', 'SMR1', 'SMR', 5000000);")


cur.execute("INSERT INTO transaksi VALUES ('TR1' , 'PREMIUM', 'SGT1', date('now'), 8000000), ('TR3' , 'VVIP', 'SMR1', date('now'), 60000000);")



db.commit()