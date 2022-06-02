import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='atm'
)
cur = db.cursor()

cur.execute("DELETE FROM transaksi WHERE noTransaksi = 'TR3' AND idNasabah = 'SMR1';")


cur.execute("DELETE FROM rekening WHERE noRekening = '3' ;")


cur.execute("DELETE FROM nasabah WHERE idNasabah = 'SMR1';")


cur.execute("DELETE FROM cabangbank WHERE kodeCabang = 'SMR';")


db.commit()