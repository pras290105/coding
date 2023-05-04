c = 1
s = int(input("MASUKAN SISI : "))
spasi = int(s / 2)
while True:
    if c % 2:
       
       print(" "*spasi + "*"*c)
       spasi -= 1
       
    c += 1
    

    if c > s:
      break

c = (s - 1)
spasi = 1
while True:
    if c % 2:
       
       print(" "*spasi + "*"*c)
       spasi += 1
       
    c -= 1
    

    if c < 1:
      break
    