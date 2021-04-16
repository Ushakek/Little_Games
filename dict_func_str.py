#Задача: нужно все ключи любого словаря сделать строками
#Мой вариант
d = {15: 2, None: 7, 1: 'Father', 5: True, (1, 6, 'string'): 15}
d_new = {}

def str_key(new_dict):
    d_new.clear()
    for i in new_dict:
        value = new_dict[i]
        key = str(i)
        d_new.update({key: value})
    return d_new

x = (str_key(d))
print('Your dict is:', x)

#Более правильный вариант, написал кто-то из студентов
def transform(slovar):
    print(type(slovar))
    tsl = {}
    for key, value in slovar.items():
        tsl[str(key)] = value
    return tsl

d = {'l': 1, 2: 45, 6: 'father'}

print(transform(d))