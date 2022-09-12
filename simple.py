from itertools import count
import numpy as np

number=np.random.randint(1,101)

#Кол-во попыток 
count = 0
print(number)
while True:
    count+=1
    user_number=int(input("Введите число:"))
    if user_number==number:
        print("Вы угадли число!" "Кол-во попыток:"+ str(count))
        break
    if user_number>number:
        print("Введенное число больше загаданного!")
    if user_number<number:
        print("Введенное число меньше загаданного!")
    