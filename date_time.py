import datetime as dt
import os 
os.system("cls")
hari_ini = dt.date.today()
print(f"Tanggal sekarang: {hari_ini}")
tanggal = int(input("Masukan Tanggal : "))
bulan = int(input("Masukan bulan : "))
tahun = int(input("Masukan tahun : "))


hasil = dt.date(tahun,bulan,tanggal)
print(hasil)
print(f"hari : {hasil:%A}")
umur = hari_ini - hasil
umur1 = umur / 365 

print(f"umurnya : {umur1.days} tahun")

