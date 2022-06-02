import cx_Oracle

db = cx_Oracle.connect(
    "admin",
    "admin",
    "127.0.0.1/XE"
)

cur = db.cursor()


cur.execute('''CREATE TABLE cabangbank (
	kodeCabang VARCHAR (3) PRIMARY KEY,
	namaCabang VARCHAR (60),
	alamatCabang VARCHAR (120))''')


cur.execute('''CREATE TABLE nasabah (
	idNasabah VARCHAR (5) PRIMARY KEY,
	namaNasabah VARCHAR (60),
	alamatNasabah VARCHAR (120))''')


cur.execute('''CREATE TABLE rekening (
	noRekening VARCHAR (9) PRIMARY KEY,
	pin VARCHAR (6),
	idNasabah VARCHAR (5),
	kodeCabang VARCHAR (3),
	saldo INTEGER,
    CONSTRAINT fk_idNasabah
	    FOREIGN KEY(idNasabah)
        REFERENCES Nasabah(idNasabah),
    CONSTRAINT fk_kodeCabang
        FOREIGN KEY(kodeCabang)
        REFERENCES CabangBank(kodeCabang))''')


cur.execute('''CREATE TABLE transaksi (
	noTransaksi VARCHAR (5) PRIMARY KEY,
	jenisNasabah VARCHAR (10),
	idNasabah VARCHAR (5),
	tanggal DATE,
	jumlah INTEGER,
    CONSTRAINT fk_trIdNasabah
        FOREIGN KEY(idNasabah)
        REFERENCES Nasabah(idNasabah))''')