import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="toko"
)

cur = db.cursor()

# hapus tr_brg
cur.execute("DELETE FROM Tr_Brg WHERE No_Nota = '02' AND Kode_Barang = 'L2';")

# hapus Barang
cur.execute("DELETE FROM Barang WHERE Kode_Barang = 'L2';")

# hapus Nota
cur.execute("DELETE FROM Nota WHERE No_Nota = '02';")

# hapus Supplier
cur.execute("DELETE FROM Supplier WHERE Kode_Supplier = '2';")

db.commit()