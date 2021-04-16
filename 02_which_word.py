import random

words = 'dog cat mouse tiger squirrel panda bear lion elephant ant horse frog sheep shark snake rabbit butterfly'.split()

def which_word(all_words):
    index_word = random.randint(0, len(all_words) - 1)
    random_word = all_words[index_word]
    return random_word

user_play = 'y'
while user_play != 'n' and user_play != 'N':
    secret_word = which_word(words)
    len_word = len(secret_word)
    win_word = []
    health = 10
    Yes_No = 'yn'

    print('Now I make a word and you need to guess it!\n I think...')
    
    for i in range(len(secret_word)):
        win_word += '_'
    print(win_word)
    
    while health != 0 and len_word !=0:
    
        game = False
        user_input = input()
        if len(user_input) > 1:
            print('Enter one letter:')

        count = 0
        for i in secret_word:
            if user_input in i:
                len_word -= 1 
                win_word[count] = user_input
                game = True
            count += 1
                
        if not game:
            health -= 1
            print('OOOOH, sorry, no this letter ', health)
        else: 
            print('Yep', win_word)

    if len_word == 0:
        print('Year! You win! The word is:', secret_word)
    else:
        print('You are died:', health, 'The word is:', secret_word)

    print('Do you whant play again?(y - yes, n - no)')
    user_play = input()
    if len(user_play) > 1 or user_play not in Yes_No:
        print('I do no undrestand, please repeat: ')
        user_play = input()