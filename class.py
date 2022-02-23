# print('========== Kumpulah Contoh Latihan ==========')

# class Titik:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
# titik_a = Titik(0,0)
# titik_b = Titik(3,4)

# print('Titik A memiliki koordinat ({}, {})'. format(titik_a.x, titik_a.y))
# print('Titik B memiliki koordinat ({}, {})'. format(titik_b.x, titik_b.y))

# class MenuMinuman:
#     def __init__(self,nama,deskripsi,harga):
#         self.nama = nama
#         self.deskripsi = deskripsi
#         self.harga = harga

# mnm1 = MenuMinuman('Jus Jambu', 'Jus Jambu Merah Tanpa Gula', 8500)
# mnm2 = MenuMinuman('Jus Alpukan Ori', 'Jus Alpukat Dengan Tambahan Air Gula Merah', 15000)
# mnm3 = MenuMinuman('Jus Alpukat Xtra Milk', 'Jus Alpukat Dengan Campuran Susu Cokelat dan Taburan Kepingan Choco', 15000)
# mnm4 = MenuMinuman('Red & Smooth', 'Smoothie pisang susu dengan strawberry', 17500)


# pilihan_minuman = [mnm1, mnm2, mnm3, mnm4]
# print('Daftar menu Healthy Fruits')
# for mn in pilihan_minuman:
#     t = '{} harga Rp {}, {}'.format(mn.nama, mn.harga, mn.deskripsi)
#     print(t)


# class Buku:
#     def __init__(self,judul, pengarang, tahun_terbit):
#         self.judul        = judul
#         self.pengarang    = pengarang
#         self.tahun_terbit = tahun_terbit

# buku = Buku('Tenggelamnya Kapal Van Der Wijck', 'HAMKA', 1938)
# t = 'Buku {} karangan{} pertama kali diterbitkan tahun {}'.format(buku.judul,buku.pengarang,buku.tahun_terbit)
# print(t)

# class Titik:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y


# class Garis:
#     def __init__(self, titik_pertama, titik_kedua):
#         self.titik_pertama = titik_pertama
#         self.titik_kedua = titik_kedua
#     def panjang(self):
#         pjg_x = self.titik_kedua.x - self.titik_pertama.x
#         pjg_y = self.titik_kedua.y - self.titik_pertama.y
#         pjg = (pjg_x**2 + pjg_y**2)**0.5
#         return pjg
# titik_a = Titik(0,0)
# titik_b = Titik(3,4)
# garis_ab = Garis(titik_a, titik_b)
# print('panjang garis ab adalah {}'.format(garis_ab.panjang()))

# class Mahasiswa:
#     def __init__(self, nama, nim, prodi,thn_masuk):
#         self.nama      = nama
#         self.nim       = nim
#         self.prodi     = prodi
#         self.thn_masuk = thn_masuk

# m1 = Mahasiswa('Udin', '10120371','Sistem Informasi',2020)
# teks = '{} adalah mahasisma {}angkatan {} dengan NIM {}'.format(m1.nama, m1.prodi, m1.thn_masuk, m1.nim)
# print(teks)

# print('=====================================================================================================')

print('========== Kumpulan Program Tugas ==========')
#Tugas Soal No 2
# class MenuMinuman:
#     def __init__(self,nama,deskripsi,harga):
#         self.nama = nama
#         self.deskripsi = deskripsi
#         self.harga = harga

# mnm1 = MenuMinuman('Jus Jambu', 'Jus Jambu Merah Tanpa Gula', 8500)
# mnm2 = MenuMinuman('Jus Alpukan Ori', 'Jus Alpukat Dengan Tambahan Air Gula Merah', 15000)
# mnm3 = MenuMinuman('Jus Alpukat Xtra Milk', 'Jus Alpukat Dengan Campuran Susu Cokelat dan Taburan Kepingan Choco', 15000)
# mnm4 = MenuMinuman('Red & Smooth', 'Smoothie pisang susu dengan strawberry', 17500)
# mnm5 = MenuMinuman('Es Jeruk', 'Es Jeruk Tambah Susu', 14000)
# mnm6 = MenuMinuman('Es Teh', 'Es Teh Tarik', 14000)


# pilihan_minuman = [mnm1, mnm2, mnm3, mnm4, mnm5, mnm6]
# print('Daftar menu Healthy Fruits')
# for mn in pilihan_minuman:
#     t = '{} harga Rp {}, {}'.format(mn.nama, mn.harga, mn.deskripsi)
#     print(t)

#Tugas Soal No 3
# class Mahasiswa:
#     def __init__(self, nama, nim, prodi,thn_masuk):
#         self.nama      = nama
#         self.nim       = nim
#         self.prodi     = prodi
#         self.thn_masuk = thn_masuk

# m1 = Mahasiswa('Udin', '10120371','Sistem Informasi',2020)
# m2 = Mahasiswa('Raden', '5210411157','Informatika',2021)
# m3 = Mahasiswa('Abel', '5210411181','Pariwisata',2021)
# mahasiswa  = [m1, m2, m3]

# for m in mahasiswa:
#     teks = '{} adalah mahasisma {}angkatan {} dengan NIM {}'.format(m.nama, m.prodi, m.thn_masuk, m.nim)
#     print(teks)


# #Tugas soal No 4
class Buku:
    def __init__(self,judul, pengarang, tahun_terbit):
        self.judul        = judul
        self.pengarang    = pengarang
        self.tahun_terbit = tahun_terbit

buku1 = Buku('Tenggelamnya Kapal Van Der Wijck', 'HAMKA', 1938)
buku2 = Buku('Laskar Pelangi', 'Andrea Hirata', 2005)
buku3 = Buku('Cantik Itu Luka', 'Eka Kurniawan', 2002)

b = [buku1, buku2, buku3]

for buku in b:
    t = 'Buku {} karangan{} pertama kali diterbitkan tahun {}'.format(buku.judul,buku.pengarang,buku.tahun_terbit)
    print(t)

# print("===============================================================================================================")