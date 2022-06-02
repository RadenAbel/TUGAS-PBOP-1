import cx_Oracle

db = cx_Oracle.connect(
    "admin",
    "admin",
    "127.0.0.1/XE"
)

cur = db.cursor()

cur.execute("DELETE FROM transaksi WHERE noTransaksi = 'TR3' AND idNasabah = 'SMR1'")


cur.execute("DELETE FROM rekening WHERE noRekening = '3'")


cur.execute("DELETE FROM nasabah WHERE idNasabah = 'SMR1'")


cur.execute("DELETE FROM cabangbank WHERE kodeCabang = 'SMR'")


db.commit()