import random
import string


key = ''.join(random.choice(string.ascii_uppercase) for i in range(10))
print(key)
a = input("MASUKAN KEY: ")
if a == key:
    print("KEY BENAR")
else:
    print("KEY SALAH ")
