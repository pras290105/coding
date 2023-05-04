import os
import datetime
import string
import random
siswa_t = {
    'nama':'nama',
    'kelas': 'kelas',
    'no.absen': 0,
    'lahir': datetime.datetime(2005,1,29)



}
data_siswa = {}
while True:
    
    os.system("cls")
    print(f"{'SELAMAT DATANG' :^20} ")
    print(f"{'DI DATA SISWA' :^20} ")
    print("="*20)

    siswa = dict.fromkeys(siswa_t.keys())
    siswa['nama'] = input("MASUKAN NAMA ANDA : ")
    siswa['kelas'] = input("KELAS : ")
    siswa['no.absen'] = input("NOMOR ABSEN : ")
    tahun_lahir = int(input("TAHUN LAHIR (EX:2005): "))
    bulan_lahir = int(input("BULAN LAHIR (EX:1-12): "))
    tanggal_lahir = int(input("TANGGAL LAHIR (EX:1-31): "))

    siswa['lahir'] = datetime.datetime(tahun_lahir,bulan_lahir,tanggal_lahir)
    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(5)))
    data_siswa.update({KEY:siswa})
    print(f"\n{'KEY':<6} {'NAMA':<17} {'KELAS':<8} {'ABSEN':^10} {'LAHIR':^10}")
    print('-'*60)

    for siswa in data_siswa:
        KEY = siswa
        NAMA = data_siswa[KEY] ['nama']
        KELAS = data_siswa[KEY] ['kelas']
        ABSEN = data_siswa[KEY] ['no.absen']
        LAHIR = data_siswa[KEY] ['lahir'].strftime("%x")

        print(f"{KEY:<6} {NAMA:<17} {KELAS:<8} {ABSEN:^10} {LAHIR:^10}")
    print("\n")
    lanjut = input("LANJUT BRO (y/n)? ")
    if lanjut == "n":
            break

