print('\n----> SINGGLE INHERITENCE <----')
class Hewan:
    def bersuara(self):
        print('kucing bersuara')

class Kucing(Hewan):
    def suara(self):
        print('meong...meong...meong')

k = Kucing()
k.suara()
k.bersuara()

print('\n----> MULTILEVEL INHERITENCE <----')
class Hewan:
    def bersuara(self):
        print('kucing bersuara')

class Kucing(Hewan):
    def Suara(self):
        print('meong...meong...meong')
    
class AnakKucing(Kucing):
    def minum(self):
        print('Minum susu')

ak = AnakKucing()

ak.bersuara()
ak.Suara()
ak.minum()

print('\n----> HIERACHICAL INHERITENCE <----')
class Induk:
    def fungsiinduk(self):
        print('fungsi pada parent class')

class anak1(Induk):
    def fungsianak1(self):
        print('fungsi pada anak 1')

class anak2(Induk):
    def fungsianak2(self):
        print('fungsi pada anak 2')

a1 = anak1()
a2 = anak2()

a1.fungsiinduk()
a1.fungsianak1()

a2.fungsiinduk()
a2.fungsianak2()



print('\n----> MULTIPLE INHERITENCE <----')
class Perhitungan:
    def penjumlahan(self, a, b):
        return a + b

class Perhitungan2:
    def perkalian(self, a, b):
        return a * b

class Hitung(Perhitungan,Perhitungan2):
    def pembagian(self, a, b):
        return a/b

h = Hitung()
print(h.penjumlahan(20,30))
print(h.perkalian(5,4))
print(h.pembagian(20,30))

class ComputerPart:
    def __init__(self, pabrikan, nama, jenis, harga):
        self.pabrikan = pabrikan
        self.nama  = nama
        self.jenis = jenis
        self.harga = harga

class Processor(ComputerPart):
    def __init__(self, pabrikan, nama, harga, jumlah_core, speed):
        super().__init__(pabrikan, nama, 'processor', harga)
        self.jumlah_core = jumlah_core
        self.speed = speed
    
class RandomAccessMemory(ComputerPart):
    def __init__(self, pabrikan, nama, harga, kapasitas):
        super().__init__(pabrikan, nama, 'RAM', harga)
        self.kapasitas = kapasitas

class HardDiskSATA(ComputerPart):
    def __init__(self, pabrikan, nama, harga, kapasitas, rpm):
        super().__init__(pabrikan, nama, 'SATA', harga)
        self.kapasitas = kapasitas
        self.rpm = rpm

p    = Processor('Intel', 'Core i7 7740X',4350000, 4,'4.2GHz')
m    = RandomAccessMemory('V-Gen', 'DDR4 SODimm PC19200/2400MHz', 328000, '4GB')
hdd  = HardDiskSATA('Seagate', 'HDD 2.5 inch', 295000, '500GB', 7200)

parts = [p,m,hdd]
for x in parts:
    print('{} {} produksi {}'.format(x.jenis, x.nama, x.pabrikan))

class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim  = nim
    
    def detailmhs(self):
        return self.nim, self.nama
    
    def cekMhs(self):
        if self.nim < 150000:
            return 'Mahasiswa aktif'
        else:
            return 'Mahasiswa tidak terdaftar'

class Siswa(Mahasiswa):
    def End(self):
        print('Mahasiswa belum melakukan daftar ulang')

mahasiswa1 = Mahasiswa('Mahasiswa 1', 135103)
print(mahasiswa1.detailmhs(), mahasiswa1.cekMhs())

mahasiswa2 = Siswa('Mahasiswa 2', 150503)
print(mahasiswa2.detailmhs(), mahasiswa2. cekMhs())
mahasiswa2.End()


class Mahasiswa():
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim  = nim

class siswa1(Mahasiswa):
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim  = nim

class siswa2(Mahasiswa):
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim  = nim

mhs1 = Mahasiswa('Mikasa', 1315105)
mhs2 = Mahasiswa('Nezuko', 135117)
mhs3 = Mahasiswa('Hancock', 134079)

print(mhs1.nama, mhs1.nim)
print(mhs2.nim)
print(mhs2.nama)

class Mahasiswa():
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim  = nim

class Siswa1(Mahasiswa):
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim  = nim

    def detSiswa1(self):
        print(self.nama, 'alamat: wall rose')

class Siswa2(Mahasiswa):
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim  = nim
    
    def detSiswa2(self):
        print(self.nama, 'jurusan: IFORMATKA')

mhs1 = Siswa1('Mikasa', 1315105)
mhs2 = Siswa2('Nezuko', 135117)

print(mhs1.nim)
mhs1.detSiswa1()

print(mhs2.nim)
mhs2.detSiswa2()

class Mahasiswa1():
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim  = nim

class Mahasiswa2():
    def __init__(self, alamat, jurusan):
        self.alamat = alamat
        self.jurusan = jurusan

class Siswa(Mahasiswa1, Mahasiswa2):
    def __init__(self, nama, nim, alamat, jurusan):
        Mahasiswa1.__init__(self, nama, nim)
        Mahasiswa2.__init__(self, alamat, jurusan)

s = Siswa('Mikasa', 135105, 'wall rose', 'INFORMATIKA')

print('nim: ---> ', s.nim, 'nama: --->',s.nama, 'alamat: --->',s.alamat, 'jurusan: --->',s.jurusan)


print('\n ----> TIGA TUGAS <----')

# Multilevel
class ComputerPart():
    def __init__(self, pabrikan, nama, jenis, harga):
        self.pabrikan = pabrikan
        self.nama  = nama
        self.jenis = jenis
        self.harga = harga

class Processor(ComputerPart):
    def __init__(self, pabrikan, nama, jenis ,harga):
        self.pabrikan = pabrikan
        self.nama  = nama
        self.jenis = jenis
        self.harga = harga
    
class HardDiskSATA(Processor):
    def __init__(self, pabrikan, nama, jenis, harga):
        self.pabrikan = pabrikan
        self.nama  = nama
        self.jenis = jenis
        self.harga = harga

class RandomAccessMemory(HardDiskSATA):
    def __init__(self, pabrikan, nama, jenis, harga):
        self.pabrikan = pabrikan
        self.nama  = nama
        self.jenis = jenis
        self.harga = harga
    
c   = ComputerPart('Intel', 'Core i7 7740X',4350000, '5GB')
p   = Processor('V-Gen', 'DDR4 SODimm PC19200/2400MHz', 328000, '4GB')
hdd = HardDiskSATA('Seagate', 'HDD 2.5 inch', 295000, '500GB')
r   = RandomAccessMemory('Intel', 'ASUS', 2346000, '10GB')
parts = [p,c,hdd,r]
for x in parts:
    print('Harga {} {} produksi {}  {} '.format(x.jenis, x.nama, x.pabrikan, x.harga ))


# Multiple
class ComputerPart():
    def __init__(self, pabrikan, nama, jenis, harga):
        self.pabrikan = pabrikan
        self.nama     = nama
        self.jenis    = jenis
        self.harga    = harga

class Processor():
    def __init__(self, jumlah_core, speed,):
        self.jumlah_core = jumlah_core
        self.speed       = speed
        
        
class RandomAccessMemory():
    def __init__(self, kapasitas):
        self.kapasitas = kapasitas

class HardDiskDATA():
    def __init__(self,rpm):
        self.rpm = rpm
        

class Computer( ComputerPart, Processor, RandomAccessMemory, HardDiskDATA ):
    def __init__(self, pabrikan, nama, jenis, harga, jumlah_core, speed, kapasitas, rpm):
        ComputerPart.__init__(self, pabrikan, nama, jenis, harga)
        Processor.__init__(self, jumlah_core, speed, )
        RandomAccessMemory.__init__(self, kapasitas)
        HardDiskDATA.__init__(self, rpm)

x = Computer('INTEL', 'ASUS', 'CORE I7', 1000, 4000, '4Ghz', '4000GB', '4000 RPM')
y = Computer('V-Gen', 'Lenovo', 'CORE I5', 1500, 5000, '5Ghz', '5000GB', '5000 RPM')
h = Computer('INTEL', 'ASUS ROG', 'CORE I7', 5000, 3000, '15Ghz', '10000GB', '6000 RPM')

z = [x ,y, h]
for v in z:
    print(f'''
           Pabrikan    : {v.pabrikan}
           Nama        : {v.nama}
           Jenis       : {v.harga}
           Jumlah_core : {v.jumlah_core}
           Speed       : {v.speed}
           Kapasitas   : {v.kapasitas}
           RPM         : {v.rpm}
           
        ''')

# Hierarchical 
class ComputerPart:
    def __init__(self, pabrikan, nama, jenis, harga):
        self.pabrikan = pabrikan
        self.nama     = nama
        self.jenis    = jenis
        self.harga    = harga

class Processor(ComputerPart):
    def __init__(self, pabrikan, nama, harga, jumlah_core, speed):
        super().__init__(pabrikan, nama, 'processor', harga)
        self.jumlah_core = jumlah_core
        self.speed       = speed
    
class RandomAccessMemory(ComputerPart):
    def __init__(self, pabrikan, nama, harga, kapasitas):
        super().__init__(pabrikan, nama, 'RAM', harga)
        self.kapasitas = kapasitas

class HardDiskSATA(ComputerPart):
    def __init__(self, pabrikan, nama, harga, kapasitas, rpm):
        super().__init__(pabrikan, nama, 'SATA', harga)
        self.kapasitas = kapasitas
        self.rpm       = rpm

class Input(ComputerPart):
    def __init__(self, pabrikan, nama, harga, mouse):
        super().__init__(pabrikan, nama, 'Mouse', harga)
        self.mouse = mouse

p    = Processor('Intel', 'Core i7 7740X',4350000, 4,'4.2GHz')
m    = RandomAccessMemory('V-Gen', 'DDR4 SODimm PC19200/2400MHz', 328000, '4GB')
hdd  = HardDiskSATA('Seagate', 'HDD 2.5 inch', 295000, '500GB', 7200)
i    = Input('Razer', 'Viper Mini', 129900000, 'False-ambidextrous')

parts = [p,m,hdd,i]
for x in parts:
    print('{} {} produksi {}'.format(x.jenis, x.nama, x.pabrikan))
