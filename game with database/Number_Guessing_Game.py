# import libraries
import random as r

# game
def game():
    winning_number = 55
    user_guessed = int(input('guess the number : '))
    turn = 1000

    while True:
        if turn == 0:
            print(f'No guesses left. The number is {winning_number}.')
            break

        elif winning_number == user_guessed:
            print('congrats you guess the number')
            break
        else:
            if winning_number > user_guessed:
                print('Too low')
            else:
                print('Too high')
            turn -= 100
        
        if turn != 0:
            user_guessed = int(input('Guess again : '))
        else:
            continue

    return turn


# update data 
def update_data(user_name,score):
    update_new_data = open('database.txt', 'a')
    update_new_data.write(f'\n{user_name},{score}')
    update_new_data.close()


# asking user for his/her name
user_name = input('Type your name : ').title()

# file open
data_file = open('database.txt', 'r')

# old data create as a dict
data_names  = {}
for names in data_file.readlines():
    name,score = names.split(',')
    data_names[name] = score


# New data create as a list
data_names2 = []
for names in data_file.readlines():
    names,score = names.split(',')
    data_names2.append(names)

# close the file
data_file.close()

# check if user name is already in database or not
    # if True 
if user_name in data_names:
    print(f'Welcome back {user_name}.\nYour last score was {data_names[user_name]}\nYou have 10 chance & 1000 points. You know the rules.\nEvery wrong guess -100 points.\nLet\'s start.\n')
    score = game()
    print(f'Your new score is {score} points.')

    # update data
    update_data(user_name,score)

    # if False
else:
    data_names2.append(user_name)
    print(f'Welcome {user_name}.\nYou have 10 & 1000 points chance to guess the number.\nYou should guess the number between 1 and 100.\nEvery wrong guess -100 points.\nLet\'s play.Good luck!\n')
    score = game()
    print(f'Your new score is {score} points.')

    # Update data
    update_data(user_name,score)



