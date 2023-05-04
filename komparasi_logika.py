#(soal 1) ---0++++5----8++++11-----
#(soal 2)+++0-----5++++8-----11+++++

print("\tsoal 1")
print("*"*(20))
print("---0++++5----8++++11-----")
input_user = float(input("masukan angka yang bernilai\nlebih dari 0 \nkurang dari 5 \nlebih dari 8 \nkurang dari 11\n =>   "))
angka1 = input_user >= 0 and input_user <= 5
angka2 =  input_user >= 8 and input_user <= 11
gabungan = angka1 or angka2
print("HASIL NYA ADALAH : ",gabungan)



print("\tsoal 2")
print("*"*(20))
print("+++0-----5++++8-----11+++++")
input_user = float(input("masukan angka yang bernilai\nkurang dari 0 \nlebih dari 5 \nkurang dari 8 \nlebih dari 11\n =>   "))
angka1 = input_user <= 0 or input_user >= 5
angka2 =  input_user <= 8 or input_user >= 11
gabungan = angka1 and angka2
print("HASIL NYA ADALAH : ",gabungan)




