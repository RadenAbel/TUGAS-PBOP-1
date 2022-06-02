import sqlite3

with sqlite3.connect('bank.db') as db:
    cur = db.cursor()

cur.execute('''CREATE TABLE cabangbank (
	kodeCabang VARCHAR(3) PRIMARY KEY,
	namaCabang VARCHAR(60),
	alamatCabang VARCHAR(120));''')


cur.execute('''CREATE TABLE nasabah ( 
	idNasabah VARCHAR(5) PRIMARY KEY,
	namaNasabah VARCHAR(60),
	alamatNasabah VARCHAR(120));''')

cur.execute('''CREATE TABLE rekening (
	noRekening VARCHAR(9) PRIMARY KEY,
	pin VARCHAR(6),
	idNasabah VARCHAR(5),
	kodeCabang VARCHAR(3),
	saldo INTEGER,
	FOREIGN KEY(idNasabah) REFERENCES Nasabah(idNasabah),
	FOREIGN KEY(kodeCabang) REFERENCES CabangBank(kodeCabang));''')


cur.execute('''CREATE TABLE transaksi (
	noTransaksi VARCHAR(5) PRIMARY KEY,
	jenisNasabah VARCHAR(10),
	idNasabah VARCHAR(5),
	tanggal DATE,
	jumlah INTEGER,
	FOREIGN KEY(idNasabah) REFERENCES Nasabah(idNasabah));''')