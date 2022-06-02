import psycopg2

db = psycopg2.connect(
    user="postgres",
    password="ABEL",
    host="localhost",
    database="bank"
)

cur = db.cursor()

cur.execute("DELETE FROM transaksi WHERE noTransaksi = 'TR3' AND idNasabah = 'SMR1';")


cur.execute("DELETE FROM rekening WHERE noRekening = '3' ;")


cur.execute("DELETE FROM nasabah WHERE idNasabah = 'SMR1';")


cur.execute("DELETE FROM cabangbank WHERE kodeCabang = 'SMR';")


db.commit()