import sqlite3

with sqlite3.connect('bank.db') as db:
    cur = db.cursor()

cur.execute("DELETE FROM transaksi WHERE noTransaksi = 'TR1' AND idNasabah = 'SGT1';")


cur.execute("DELETE FROM rekening WHERE noRekening = '1' ;")


cur.execute("DELETE FROM nasabah WHERE idNasabah = 'SGT1';")


cur.execute("DELETE FROM cabangbank WHERE kodeCabang = 'SGT';")


db.commit()