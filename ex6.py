# Задача 6: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, 
# которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

num1 = int(input("Введите первые 3 цифры билета: "))
num2 = int(input("Введите вторые 3 цифры билета: "))

total1 = 0
while num1 > 0:
    lastNum = num1 % 10
    total1 += lastNum
    num1 //= 10   

total2 = 0
while num2 > 0:
    lastNum = num2 % 10
    total2 += lastNum
    num2 //= 10
   
if total1 == total2:
    print("Билетик счастливый!")

elif  total1 != total2:
    print("Билетик не счастливый :( ")  
    

