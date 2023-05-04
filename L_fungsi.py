import os
import datetime


def header():
    print("==============================================")
    print("PROGRAM HITUNG LUAS & KELILING PERSEGI PANJANG")
    waktu = datetime.datetime.now()
    print(waktu.strftime("Tme Now : %A,%d-%B-%Y|%H:%M %p"))
    print("==============================================")

def user():
    lebar = int(input("Masukan Lebarnya: "))
    panjang = int(input("Masukan Panjangnya: "))
    return lebar,panjang
def luas(lebar,panjang):
    return lebar * panjang
def keliling(lebar,panjang):
    return 2 * (lebar + panjang)

while True:
    os.system("cls")
    header()
    LEBAR,PANJANG = user()
    KELILING = keliling(LEBAR,PANJANG)
    LUAS = luas(LEBAR,PANJANG)
    print(f"HASIl KELILINGNYA: {KELILING}")
    print(f"HASIl LUASNYA: {LUAS}")
    lnjut = input("MAU LANJUT? y/n: ")
    if lnjut == "n":
        break
    else:
        print("PILIH HURUF YANG BENAR!!!")
print("THANKYOU............. :)")
