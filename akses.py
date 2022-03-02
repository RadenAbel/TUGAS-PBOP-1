print('\n-- Akses Public Segitiga --')
class Segitiga:
    def __init__(self, alas, tinggi):
        self.alas   = alas
        self.tinggi = tinggi
        self.luas   = 0.5 * alas * tinggi
segitiga_besar = Segitiga(100, 80)

print("alas : ", segitiga_besar.alas)
print("tingi: ", segitiga_besar.tinggi)
print("luas : ", segitiga_besar.luas)
print("\n------------------------------------------------------------------------------------------------------------")

print('\n-- Akses Protected Utama dan Turunan --')
class Utama:
    def __init__(self):
        self._a = 2

class Turunan(Utama):
    def __init__(self):
        Utama.__init__(self)
        print("Memanggil variabel protected pada class utama: ", self._a)
        
        #Memodifikasi variabel protected
        self._a = 3
        print("Memanggil variabel protected yang dimodifikasi diluar kelas: ", self._a)

ob1 = Turunan()
ob2 = Utama()

print("Mengakses variabel dari objek1: ", ob1._a)
print("Mengakses variabel dari objek2: ", ob2._a)
print("\n------------------------------------------------------------------------------------------------------------")

print('\n-- Akses Private Hitung --')
class Hitung:
    def __init__(self):
        self.__angkarahasia = 0

    def tampilkanHitung(self):
        self.__angkarahasia +=1
        print(self.__angkarahasia)

hitungan = Hitung()
hitungan.tampilkanHitung()

hitungan.tampilkanHitung()
print("\n------------------------------------------------------------------------------------------------------------")


print('\n-- Kumpulan Akses Mobil --')
#public
class Mobil:
    def __init__(self, jendela, pintu, mesin):
        self.jendela = jendela
        self.pintu   = pintu
        self.mesin   = mesin

mobil = Mobil(4, 4, "Diesel")
print('Jendela--> ', mobil.jendela)
print('Pintu  --> ', mobil.pintu)
print('Mesin  --> ', mobil.mesin)

#protected
class Mobil:
    def __init__(self, jendela, pintu, mesin):
        self._jendela = jendela
        self._pintu   = pintu
        self._mesin   = mesin
        

class Truk(Mobil):
    def __init__(self, jendela, pintu, mesin, tipe):
        super().__init__(jendela, pintu, mesin)
        print('Jendela: ', )
        self.tipeBak = tipe

#private
class Mobil:
    def __init__(self, jendela, pintu, mesin):
        self._Mobil__jendela = jendela
        self._Mobil__pintu   = pintu
        self._Mobil__mesin   = mesin

mobil1 = Mobil(2, 2, "2JZ-GTE")
mobil2 = Mobil(4, 4, "Diesel")

mobil = [mobil1, mobil2]
for mbl in mobil:
    jns = 'Mobil ini memiliki {} pintu dan {} jendela serta dilengkapi dengan mesin {}'.format(mbl._Mobil__pintu , mbl._Mobil__jendela, mbl._Mobil__mesin )

    print(jns)

print("\n------------------------------------------------------------------------------------------------------------")


print('\n-- Latihan Semua Hak Akses --')
class pegawai:
    __nama   = ''
    __alamat = ''
    __gaji   = 0

    def __init__(self, nama, alamat):
        self.__nama = nama
        self.__alamat = alamat

    def __hitungGaji(self):
        upahLembur = 20000
        gajiPokok  = 2000000
        jumLembur  = int(input("Total jam lembur: "))
        self.__gaji= (upahLembur * jumLembur) + gajiPokok

    def tampilDetail(self):
        print("\n--Menghitung dan menampilkan detail Gaji pegawai--")
        print("Nama       : ", self.__nama)
        print("Alamat     : ", self.__alamat)
        self.__hitungGaji()
        print("Total Gaji : ", self.__gaji)

pgw1 = pegawai("Mikas Ackerman","wall Rose")
pgw1.tampilDetail()

pgw2 = pegawai("Saya Kisaragi", "prefektur Nagano")
pgw2.tampilDetail()
print("\n------------------------------------------------------------------------------------------------------------")

print('\n-- Akses Private MenuMinuman --')
class MenuMinuman:
    def __init__(self,nama,deskripsi,harga, ukuran):
        self.nama      = nama
        self.deskripsi = deskripsi
        self.harga     = harga
        self._MenuMinuman__ukuran = ukuran

mnm1 = MenuMinuman('Jus Jambu', 'Jus Jambu Merah Tanpa Gula', 8500, "Smaall")
mnm2 = MenuMinuman('Jus Alpukan Ori', 'Jus Alpukat Dengan Tambahan Air Gula Merah', 15000, "Large")
mnm3 = MenuMinuman('Jus Alpukat Xtra Milk', 'Jus Alpukat Dengan Campuran Susu Cokelat', 15000, "Medium")
mnm4 = MenuMinuman('Red & Smooth', 'Smoothie pisang susu dengan strawberry', 17500, "Medium")


pilihan_minuman = [mnm1, mnm2, mnm3, mnm4]
print('Daftar menu Healthy Fruits')
for mn in pilihan_minuman:
    t = '{} harga Rp {}, {}, ukuran --> {}'.format(mn.nama, mn.harga, mn.deskripsi, mn._MenuMinuman__ukuran)
    print(t)
print("\n------------------------------------------------------------------------------------------------------")

print("\n-- Akses Private Buku --")
class Buku:
    def __init__(self,judul, pengarang, tahun_terbit, harga):
        self.judul        = judul
        self.pengarang    = pengarang
        self.tahun_terbit = tahun_terbit
        self._Buku__harga      = harga

buku1 = Buku('Tenggelamnya Kapal Van Der Wijck', 'HAMKA', 1938, 35000)
buku2 = Buku('Laskar Pelangi', 'Andrea Hirata',  2005, 40000)
buku3 = Buku('Cantik Itu Luka', 'Eka Kurniawan', 2002, 50000)

b = [buku1, buku2, buku3]

for buku in b:
    t = 'Buku {} karangan {} pertama kali diterbitkan tahun {} dengan harga --> {}'.format(buku.judul,buku.pengarang,buku.tahun_terbit, buku._Buku__harga)
    print(t)

print("\n------------------------------------------------------------------------------------------------------------")

print("\n-- Akses Private Mahasiswa --")
class Mahasiswa:
    def __init__(self, nama, nim, prodi,thn_masuk, asal_kota):
        self.nama               = nama
        self.nim                = nim
        self.prodi              = prodi
        self.thn_masuk          = thn_masuk
        self._Mahasiswa__asal_kota = asal_kota

m1 = Mahasiswa('Udin' , '10120371'  ,'Sistem Informasi',2020,  'BANDUNG')
m2 = Mahasiswa('Raden', '5210411157','Informatika'     ,2021,  'SANGATTA')
m3 = Mahasiswa('Abel' , '5210411181','Pariwisata'      ,2021,  'BALIKPAPAN')
mahasiswa  = [m1, m2, m3]

for m in mahasiswa:
    teks = '{} adalah mahasisma {} angkatan {} berasal dari kota {} dengan NIM {}'.format(m.nama, m.prodi, m.thn_masuk,m._Mahasiswa__asal_kota, m.nim)
    print(teks)
print("\n------------------------------------------------------------------------------------------------------------")