import psycopg2

db = psycopg2.connect(
    user="postgres",
    password="ABEL",
    host="localhost",
    database="toko"
)

cur = db.cursor()

# update supplier
cur.execute("UPDATE Supplier SET Nama_Supplier = 'NARUTO' WHERE Kode_Supplier = '1';")

# update Nota
cur.execute("UPDATE Nota SET Total = 13000000 WHERE No_Nota = '02';")

# update barang
cur.execute("UPDATE Barang SET Nama_Barang = 'RAZER' WHERE Kode_Barang = 'L2'; ")

# update tr_brg
cur.execute("UPDATE Tr_Brg SET Harga = 22000000 WHERE Kode_Barang = 'L1' AND No_Nota = '01';")


db.commit()