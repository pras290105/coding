#kasus gabungan 
#++++++++3-----------
input_user = int(input("Masukan angka kurang dari 3 atau lebih besar dari 10 :"))
kurang_dari = input_user < 3
print("kurang dari 3 :" , kurang_dari)
lebih_dari = input_user > 10
print("lebih besar dari 10 :" ,lebih_dari)
 
#gabungan +++++++3--------10++++++++
hasil_gabungan = kurang_dari or lebih_dari
print("Jika di or kan hasilnya adalah " ,hasil_gabungan)
#kasus irisan
input_user = int(input("Masukan angka lebih dari 3 dan kurang dari 10 \n:"))
#------3+++++++
lebih_dari = input_user > 3
print("lebih dari 3 : " , lebih_dari)
#+++++++10-------
kurang_dari = input_user < 10
print("kurang dari 10 : " , kurang_dari)
hasil_irisan = lebih_dari and kurang_dari
print("jika di and kan hasilnya adalah " ,hasil_irisan)


    