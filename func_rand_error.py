#Задача: поймать рандомную ошибку
import  random

def rand_err():
    error_types = {1: ValueError, 2: TypeError, 3: RuntimeError}
    raise error_types[random.randint(1, 3)]

try: 
    rand_err()
except ValueError:
    print('поймали ValueError')
except TypeError:
    print('поймали TypeError')
except RuntimeError:
    print('поймали RuntimeError')