from ast import Break
import csv 
import os
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    while(True):
        print("1. Cari Buku")
        print("2. Cari Majalah")
        print("3. Cari DVD")
        print("4. Cari Manga")
        print("5. List Buku")
        print("6. Keluar Aplikasi")
        try:
            menu = int(input("Input pilihan menu sesuai yang anda inginkan ---> "))
            print()
            if(menu == 1):
                s_book()
            
            elif(menu == 2):
                s_majalah()

            elif(menu == 3):
                s_DVD()
            
            elif(menu == 4):
                s_manga()


            elif(menu == 5):
                list_book()

            elif(menu == 6):
                keluar()
                break
            
            else:
                print("Masukan pilihan menu yang anda inginkan")
                continue

        except ValueError:
            print("masukkan sesuai petunjuk !")
            # kembali()
            continue

def s_book():
    with open('data_buku_perpus.txt') as temp_f:
        data_b = temp_f.readlines()
        search = str(input("Masukkan judul buku yang anda ingin cari ---> "))
    for b in data_b:
        if search in b:
            return True, print(b,"---------- Buku yang anda cari tersedia ----------")
    return False, print("Maaf buku yang anda cari tidak tersedia")

def s_majalah():
    with open('data_buku_perpus.txt') as temp_f:
        data_m = temp_f.readlines()
        search = str(input("Masukkan judul buku yang anda ingin cari ---> "))
    for m in data_m:
        if search in m:
            return True, print(m,"---------- Buku yang anda cari tersedia ----------")
    return False, print("Maaf buku yang anda cari tidak tersedia")

def s_DVD():
    with open('data_buku_perpus.txt') as temp_f:
        data_D = temp_f.readlines()
        search = str(input("Masukkan judul buku yang anda ingin cari ---> "))
    for D in data_D:
        if search in D:
            return True, print(D,"---------- Buku yang anda cari tersedia ----------")
    return False, print("Maaf buku yang anda cari tidak tersedia")

def s_manga():
    with open('data_buku_perpus.txt') as temp_f:
        data_mn = temp_f.readlines()
        search = str(input("Masukkan judul buku yang anda ingin cari ---> "))
    for mn in data_mn:
        if search in mn:
            return True, print(mn,"---------- Buku yang anda cari tersedia ----------")
    return False, print("Maaf buku yang anda cari tidak tersedia")

def list_book():
    with open('data_buku_perpus.txt', 'r+') as f:
        list = f.read()
        print(list)
        print()

def keluar():
    print("----- Terimakasih Telah menggunakan sistem kami :) -----")


main_menu()