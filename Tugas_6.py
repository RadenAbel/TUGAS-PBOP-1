# Overloading
# class ComputerPart:
#     def __init__(self, pabrikan, nama):
#         self.pabrikan = pabrikan
#         self.nama     = nama
    
#     def detComputer(self):
#         print('Pabrikan: ', self.pabrikan, 'nama: ', self.nama)

#     def HitungHarga(self, harga=None):
#         if harga != None:
#             h = harga
#             print('Harga: ', h)
#         else:
#             print('Tidak ada pesanan')

# com1 = ComputerPart('ASUS', 'ROG STRIX')
# com2 = ComputerPart('ASUS', 'TUF GAMING')
# com1.detComputer()
# com2.detComputer()
# com1.HitungHarga(100000)
# com2.HitungHarga(200000)

# Overriding
class ComputerPart:
    def __init__(self, pabrikan, nama):
        self.pabrikan = pabrikan
        self.nama     = nama
    
    def detComputer(self):
        print('Nama:',self.nama,'Harga: Rp.1000000')

class ComputerPart_2(ComputerPart):
    def __init__(self, pabrikan, nama):
        self.pabrikan = pabrikan
        self.nama     = nama
    
    def detComputer(self):
        print('Nama:',self.nama,'Harga: Rp.200000000')

com1 = ComputerPart_2('Asus'  , 'ROG STRIX PRO')
com2 = ComputerPart(  'Asus'  , 'TUF GAMING PRO')

print(com1.pabrikan, com1.nama)
com1.detComputer()

print(com2.pabrikan, com2.nama)
com2.detComputer()
