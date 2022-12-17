# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6,782 -> 23
# - 0,56 -> 11

def summa(number):
    summa = 0
    for i in number:
        if i != '.':
            summa = summa + int(i)
    return summa
number = input('Введите вещественное число: ')
print(summa(number))