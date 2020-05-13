# import libraries
import random as r

# game
def game():
    user_said = input(f'{user_name} do you want to play (Y/N) : ').lower()
    turn2 = 0
    y_said = 0
    while True:

        if ('y' not in user_said) and ('n' not in user_said) and (user_said != True):
            user_said = input('Invalid keyword. Type again : ')

        elif 'y' in user_said:
            print('Let\'s play.Good luck!\n')
            winning_number = r.randint(1,100)
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
                    print(f'{turn} points left.')
                
                if turn != 0:
                    user_guessed = int(input('Guess again : '))
                else:
                    continue
            print(f'Score = {turn}\n')
            user_said = input(f'{user_name} do you want to play more (Y/N) : ')
            turn2 += turn
            y_said += 1

        else:
            break

    return turn2, y_said


# update data 
def update_data(user_name,score,game_played):
    update_new_data = open('database.txt', 'a')
    update_new_data.write(f'\n{user_name},{score},{game_played}')
    update_new_data.close()


# asking user for his/her name
user_name = input('Type your name : ').title()

# file open
data_file = open('database.txt', 'r')

# old data create as a dict
data_names  = {}
# new data
data_names2 = []
data_game_play = [] # for finding last gameplayed
for names in data_file.readlines():
    name,score,g = names.split(',')
    data_names[name] = score
    data_names2.append(name)
    
    if user_name in name:
        data_game_play.append(int(g))

# close the file
data_file.close()

# check if user name is already in database or not
    # if True 
if user_name in data_names:
    print(f'\nWelcome back {user_name}.\nYour last score was {data_names[user_name]} in {data_game_play[-1]} games.\nYou know the rules 10 chance & 1000 points.\n')
    score, game_played = game()
    print(f'You scored {score} points in {game_played} games.')
    print(f'Ok bye {user_name}. See you soon')

    # update data
    update_data(user_name,score,game_played)

    # if False
else:
    data_names2.append(user_name)
    print(f'\nWelcome {user_name}.\nYou have 1000 points & 10 chance to guess the number.\nYou should guess the number between 1 and 100.\nEvery wrong guess -100 points.\n')
    score, game_played = game()
    print(f'You scored {score} points in {game_played} games.')
    print(f'Ok bye {user_name}. See you soon')
    

    # Update data
    update_data(user_name,score,game_played)