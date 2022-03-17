# print(len("polymorphism"))
# print(len([0,1,2,3]))

# '''

# Menggunakan fungsi len
# Output:
# 12 (Tipe Data String)
# 4 (Tipe Data List)
# '''

# class jerman:
#     def ibukota(self):
#         print('Berlin adalah ibukota negara Jerman')

# class jepang:
#     def ibukota(self):
#         print('Tokyo adalah ibukota jepang')

# negara_1 = jerman()
# negara_2 = jepang()

# for country in (negara_1, negara_2):
#     country.ibukota()



# class Kucing:
#     def __init__(self, nama, umur):
#         self.nama = nama
#         self.umur = umur

#     def bersuara(self):
#         print('Meow')

# class Dog:
#     def __init__(self, nama, umur):
#         self.nama = nama 
#         self.umur = umur

#     def bersuara(self):
#         print('Guk...guk...')

# kucing1 = Kucing("Tom", 3)
# anjing1 = Dog("Spike", 4)

# for hewan in (kucing1, anjing1):
#     hewan.bersuara()

# class burung:
#     def intro(self):
#         print("Di dunia ini ada beberapa type berbeda dari spesies burung")

#     def terbang(self):
#         print("Hampir semua burung dapat terbang, namun ada beberapa yang tidak dapat terbang")

# class Elang(burung):
#     def terbang(self):
#         print("Elang dapat terbang")

# class BurungUnta(burung):
#     def terbang(self):
#         print("Burung unta tidak dapat terbang")

# obj_burung = burung()
# obj_elang = Elang()
# obj_burung_unta = BurungUnta()

# obj_burung.intro()
# obj_burung.terbang()

# obj_elang.intro()
# obj_elang.terbang()

# obj_burung_unta.intro()
# obj_burung_unta.terbang()

# from abc import ABC, abstractmethod
# class Bentuk(ABC):
#     @abstractmethod
#     def luas(self):
#         return self.__sisi * self.__sisi

#     @abstractmethod
#     def keliling(self):
#         return 4 * self.__sisi

# class Persegi(Bentuk):
#     def __init__(self, sisi):
#         self.__sisi = sisi
#     def luas(self):
#         return self.__sisi * self.__sisi
#     def keliling(self):
#         return 4 * self.__sisi

# persegi = Persegi(6)
# print(persegi.luas())
# print(persegi.keliling())

# class Pegawai:
#     jumlah = 0

#     def __init__(self, nama, gaji):
#         self.nama = nama
#         self.gaji = gaji
#         Pegawai.jumlah += 1

#     def tampilJumlah(self):
#         print("Total pegawai", Pegawai.jumlah)

#     def tampilpegawai(self):
#         print("Nama: ", self.nama, ", gaji:", self.gaji)

#     def tunjangan(self, istri=None, anak=None):
#         if anak != None and istri != None:
#             total = anak + istri
#             print("Tunjangan anak + istri =", total)
#         else:
#             total = istri
#             print("Tunjangan istri =", total)

# peg1 = Pegawai("Eren", 2000)
# peg2 = Pegawai("Luffy", 6000)
# peg1.tampilpegawai()
# peg2.tampilpegawai()
# peg1.tunjangan(2500,2000)
# peg2.tunjangan(2500)

# print("Total pegawai %d" % Pegawai.jumlah)
# rataGaji = (peg1.gaji + peg2.gaji)/Pegawai.jumlah
# print("Rata-rata gaji ="+ str(rataGaji))

# class Segiempat():
#     def __init__(self, panjang, lebar):
#         self.panjang = panjang
#         self.lebar   = lebar

#     def hitungLuas(self):
#         print("Luas Segiempat =", self.panjang * self.lebar, "m^2")
    
# class Bujursangkar(Segiempat):
#     def __init__(self, sisi):
#         self.side = sisi
#         Segiempat.__init__(self, sisi, sisi)

#     def hitungLuas(self):
#         print("Luas bujur sangkar =", self.side*self.side, "m^2")

# b = Bujursangkar(4)
# s = Segiempat(2,4)
# b.hitungLuas()
# s.hitungLuas()

# class Mahasiswa:
#     def __init__(self, nama, nim):
#         self.nama = nama
#         self.nim = nim

#     def tampilMhs(self):
#         print("Nama:", self.nama, ", nim:", self.nim)
    
#     #   Method Overloading
#     def hitungSKS(self, jmlsks=None, sks=None):
#         if jmlsks !=None and sks!=None:
#             totalsks = jmlsks + sks
#             print("Total sks =", totalsks)
#         else:
#             totalsks = jmlsks
#             print("Total sks =", totalsks)

#         if totalsks >= 100:
#             print("Diperbolehkan mengambil skripsi")
        
#         else:
#             print("Tidak diperbolehkan mengambil skripsi")

# mhs1 = Mahasiswa("Eren", 123180015)
# mhs2 = Mahasiswa("Luffy", 123190007)
# mhs1.tampilMhs()
# mhs2.tampilMhs()
# mhs1.hitungSKS(80, 34)
# mhs2.hitungSKS(83)

class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def detSiswa(self):
        print(self.nama, 'alamat: wall rose')

class Siswa(Mahasiswa):
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim  = nim

    def detSiswa(self):
        print(self.nama, 'Jurusan: Informatika')

mhs1 = Siswa('Mikasa', 135105)
mhs2 = Mahasiswa('Nezuko', 135119)

print(mhs1.nim, mhs1.nama)
mhs1.detSiswa()
print(mhs2.nim, mhs2.nama)
mhs2.detSiswa()