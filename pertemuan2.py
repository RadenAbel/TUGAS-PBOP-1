str1 = "aku cinta indonesia"
print(str1)

str2 = str1[:10]+'tanah airku'+str1[9:]
print(str2)

str3 = 'aku cinta tanah air ku indonesia'
str4 = str3[:9]+''+str3[22:]
print(str4)

kelas = 'Praktikum Pemrograman Berorientasi Objek'
up = kelas.upper()
lo = kelas.lower()
print(kelas)
print(up)
print(lo)

s = '     python     '
print(s.strip())
print(s.lstrip())
print(s.rstrip())

print(len(kelas))

jumlah = len(kelas)
print('panjang string adalah :',jumlah)

s1 = 'python '
s2 = 'programing'
print(s1+s2)

print(kelas.index('a'))
print(kelas)

kelas2 = kelas.replace('Praktikum','praktik')
print(kelas2)

a = 'satu'
b = 'dua'
c = 'tiga'
print('saya mempunyai %s mangga'%(b))

print(kelas.split())

# input1 = input('hari ini adalah : ')
# print(input1)

# data1 = input('angka 1 : ')
# data2 = input('angka 2 : ')
# data3 = int(data1)+int(data2)
# print(data1,' * ',data2,' = ',data3)

list1 = [1,2,3,4,5,6,7,8,9]
# print(list1)
# print(list1[5])
# print(list1[:3])
# print(len(list1))
# print(list1[10-3:])
# print(list1[2:9])
# print(list1[-10])
# print(list1[0])
# list1.append(10)
# print(list1)
# list1.insert(1,11)
# print(list1)

list2 = ['hello']
list1.extend(list2)
print(list1)

list1.extend('hai')
print(list1)

del list1[1]
print(list1)

list1.remove(5)
print(list1)

list1.pop()
print(list1)

a = [50,20,30,40]
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)
print(min(a))
print(max(a))
d = {1:100,2:200,3:300,4:400,5:500}
print(d)
print(d[2])
print(d.get(4))
print(d.keys())
print(d.values())
del d[3]
print(d)
d.clear()
len(d)

t = (100,200,300,400)
print(t[0])
print(t[3])
f = t.index(200)
print(f)
t2=(10,20,10,30,10,40,20)
print(t2.count(20))
print(t2.count(10))
print(t2.count(30))


#set atau himpunan
car = {"AVANZA", "BMW", "LAMBORGINI","TESLA"}
x   = set(car)
print(x)
print("=========================================")

print("========== FUNGSI ADD ATAU UDATE ==========")
car = {"AVANZA", "BMW", "LAMBORGINI","TESLA"}
car.add("SUPRA")
print(car)
print("=========================================")

print("========== FUNGSI CLEAR ==========")
car = {"AVANZA", "BMW", "LAMBORGINI","TESLA"}
car.clear()
print(car)
print("=========================================")

print("========== FUNGSI COPY ==========")
car   = {"AVANZA", "BMW", "LAMBORGINI","TESLA"}
car_2 = car.copy()
print(car_2)
print("=========================================")

print("========== FUNGSI INTERSECTION ==========")
genap  = {2, 4, 6, 8, 10}
ganjil = {1, 3, 5, 7, 9}
prima  = {2, 3, 5, 7}
print(ganjil.intersection(prima))
print("=========================================")

print("========== FUNGSI DIFFERENCE ==========")
car    = {"AVANZA", "BMW", "LAMBORGINI","TESLA"}
car_2  = {"AVANZA", "BMW", "SUPRA", "GTR", "LAMBORGINI"}
d1     = car.difference(car_2)
d2     = car_2.difference(car)
print(d1, "---->", d2)
print("=========================================")

print("========== FUNGSI UNION ==========")
genap    = {2, 4, 6, 8, 10}
ganjil   = {1, 3, 5, 7, 9}
gabungan = ganjil.union(genap)
print(gabungan)
print("=========================================")

print("========== FUNGSI FROZENSET ==========")
car    = {"AVANZA", "BMW", "LAMBORGINI","TESLA"}
fcar   = frozenset(car)
print(fcar)
print("=========================================")