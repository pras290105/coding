

while True:
    
    print("\t\tPROGRAM KONVERSI SUHU")
    print("\t\t=====================")
    print("1. CELCIUS\n2. REAMUR\n3. FAHRENHEIT\n4. KELVIN\n")
    data = int(input("pilih suhu:"))

    if data == 1: 
       data1 = float(input("masukan suhu dalam celcius: "))
       reamur = (4/5) * data1
       print("suhu dalam reamur = ",reamur,"r")
       fahrenheit = ((9/5) * data1) + 32
       print("suhu dalam fahrenheit = ",fahrenheit,"f")
       kelvin = data1 + 273
       print("suhu dalam kelvin = ",kelvin,"k")
    elif data == 2:
         data2 = float(input("masukan suhu dalam reamur: "))
         celcius = 5/4 * data2
         print("suhu dalam celcius = ",celcius,"c")
         fahrenheit = (9/4 * data2) + 32
         print("suhu dalam fahrenheit = ",fahrenheit,"f")
         kelvin = 5/4 * data2 + 273
         print("suhu dalam kelvin = ",kelvin, "k")
    elif data == 3:
         data3 = float(input("masukan suhu dalam fahrenheit: "))
         celcius = 5/9 * (data3 - 32)
         print("suhu dalam celcius = ",celcius,"c")
         reamur = 4/9 * (data3 - 32)
         print("suhu dalam reamur = ",reamur,"r")
         kelvin = 5/9 * (data3 - 32) + 273
         print("suhu dalam kelvin = ",kelvin, "k")
    elif data == 4:
         data4 = float(input("masukan suhu dalam kelvin: "))
         celcius = data4 - 273
         print("suhu dalam celcius = ",celcius,"c")
         reamur = 4/5 * (data4 - 273)
         print("suhu dalam reamur = ",reamur,"r")
         fahrenheit = 9/5 * (data4 - 273) + 32
         print("suhu dalam fahrenheit = ",fahrenheit, "f")
    c = input("apakah anda ingin mengkonversi lagi? ya / tidak: ")
    if c == "tidak":
        break    
print("terimakasih")

