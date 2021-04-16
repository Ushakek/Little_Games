#Задача: фильтр листа, если есть не int значения, то выводить ошибку
l = [1, 2, 4, 'zero', '1', 5, 6, 7]
l_correct = [8, 17, 1, 45, 15, 6, 21, 5]

print('l =', l, '\n', 'l_correct =', l_correct)

def filtr_int(new_list):
        try:
            for i in new_list:
                int(i)
        except ValueError as e:
            print('Error!', end = ' ')
            return e
        else:
            new_list.sort()
        return new_list

x = filtr_int(l_correct)
print(x, '\n')
y = filtr_int(l)
print(y, '\n')