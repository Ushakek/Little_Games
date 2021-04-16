#Задача: суммирование любого количества чисел, здесь же умножение любого количества заданых чисел
def sum_all(*num):
    print(num, 'Summing...')
    print('sum is:', sum(num))


sum_all(4, 5, 7, 10, 12, 45)

def multi(*num):
    z = 1
    for i in num:
        z *= i
    return z

x = multi(1, 2, 3)
print('multiplication is:', x)