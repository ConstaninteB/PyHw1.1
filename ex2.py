# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = int(input("Введите трехзначное число: "))

if number <= 999:  
  num1 = number // 100
  num2 = number // 10 % 10
  num3 = number % 10
  print("Cумма цифр: ", num1 + num2 + num3)
else:
 print("Вы ввели некорректное число ")  
