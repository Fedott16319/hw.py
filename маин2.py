# Найти сумму чисел списка стоящих на нечетной позиции

def F(ls, count=-1):
    if count == -1:
        return sum(ls[1::2])
    else:
        return sum(ls[1:count:2])


a = list(map(int, input("Введите числа через пробел: ").split()))
b = F(a)
print(b)

