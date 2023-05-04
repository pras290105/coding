
import os
os.system("cls")
list_buku = []
print("\t_____________________________________")
print("\tSELAMAT DATANG DI PERPUSTAKAAN ONLINE")
print("\t_____________________________________")
while True:
    print("\nMASUKAN DATA BUKU  ")
    print("_____________________\n")
    judul = input("JUDUL BUKU \t: ")
    penulis = input("PENULISNYA \t: ")
    buku_baru = [judul,penulis]
    list_buku.append(buku_baru)
    print("\nLIST BUKU")
    print("============\n")
 
    for index,buku in enumerate(list_buku):
       
        print(f"{index+1}. JUDUL BUKU \t: {buku[0]} \n   PENULIS \t: {buku[1]} \n")
    lanjut = input("\nMau lanjut (y/n) ? ")
    if lanjut == "n":
        break
        
    