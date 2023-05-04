import os
os.system('cls')
nama = input("Masukan nama anda : ")
nama = nama.upper()
judul = f"SELAMAT DATANG {nama} DI PROGRAM KALKULATOR SEDERHANA"
b = len(judul)
print("="*b)
print(judul)
print("="*b)

print("SILAHKAN PILIH OPERASI : ")
print("1. PERTAMBAHAN (+)\n2. PENGURANGAN (-)\n3. PERKALIAN (*)\n4. PEMBAGIAN (/)")
operasi = input("PILIH DENGAN ANGKA --> ")
angka1 = float(input("SILAHKAN MASUKAN ANGKA KE 1 : "))
angka2 = float(input("SILAHKAN MASUKAN ANGKA KE 2 : "))
if operasi == '1':
    hasil = angka1 + angka2
    print(f"HASILNYA ADALAH : {hasil}")
elif operasi == '2':
    hasil = angka1 - angka2
    print(f"HASILNYA ADALAH : {hasil}")
elif operasi == '3':
    hasil = angka1 * angka2
    print(f"HASILNYA ADALAH : {hasil}")
elif operasi == '4':
    hasil = angka1 / angka2
    print(f"HASILNYA ADALAH : {hasil}")
else:
    print("MASUKAN OPERASI DENGAN BENAR")
print(f"TERIMAKASIH {nama}")
print(f"TERIMAKASIH {nama}")

     
    
