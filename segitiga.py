c = 1
sisi = int(input("MASUKAN SISI : "))
spasi = int(sisi / 2)

while True:
    if c % 2:
        print(" "*spasi , "*"*c)
        spasi -= 1
    c += 1
    if c > sisi:
        break