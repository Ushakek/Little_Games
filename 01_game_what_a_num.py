import random

def rand_num():
    x = random.randint(1, 10)
    return x

print('Hi, today I gonna play with you. Now i will think about number, and you will go guess this number\n I think...')

user_exit = 'y'
while user_exit != 'n' and 'N':
    my_num = rand_num()
    print('You can start!')
    user_input = 0
    while user_input != my_num:
        try:
            user_input = int(input())
            if user_input > my_num:
                print('My number is less')
            elif user_input < my_num:
                print('My number is bigger')
        except ValueError:
            print('Sorry, try again')
    
    print('You are right! Do you whant play again? (Yes - y, No - n)')
    user_exit = input()