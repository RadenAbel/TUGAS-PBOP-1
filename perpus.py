class perpusitem:
    def __init__(self, judul, subjek, lokasi, info):
        self.judul  = judul
        self.subjek = subjek
        self.lokasi = lokasi
        self.info   = info

        ''' def lokasiSimpan(self):
            self.lokasi = lokasi
            self.info   = info
        '''
class Buku(perpusitem):
    def __init__(self, judul, subjek, lokasi, info, isbn, pengarang, jmlhal, ukuran):
        super().__init__(judul, 'Buku', lokasi, info)
        self.isbn      = isbn
        self.pengarang = pengarang
        self.jmlhal    = jmlhal
        self.ukuran    = ukuran


class Majalah(perpusitem):
    def __init__(self, judul, subjek, lokasi, info, volume, issue):
        super().__init__(judul, 'Majalah', lokasi, info)
        self.volume = volume
        self.issue  = issue 

class DVD(perpusitem):
    def __init__(self, judul, subjek, lokasi, info, aktor, genre):
        super().__init__(judul, 'DVD', lokasi, info)
        self.aktor = aktor
        self.genre = genre

b = Buku('Pemrograman Python', 'Buku Cetak', 'RaK Nomor 1', 'dipinjam', '945-884-98-02', 'Yogi Syarif', 2, '25x15')
m = Majalah('Dunia Komputer', 'Majalah Cetak', 'Rak Nomor 2', 'ada', 'VII', 'Komputer')
d = DVD('Shingeki No Kyojin','softcopy','Rak Nomor 3','ada','mikasa','anime')

daftar = [b,m,d]
for dft in daftar:
    print('{} {} {} {}'.format(dft.judul, dft.subjek, dft.lokasi, dft.info))
