car = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
import random
con=int(input("ingrese la longitud de la contraseña"))
password = ""
for i in range(con):
    password+=random.choice(car)
print(password)
    
