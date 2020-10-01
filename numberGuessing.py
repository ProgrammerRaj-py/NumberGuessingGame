from random import randint

# welcome screen
user_name = input('Type your name : ').title()
print(f'Hello {user_name}.')

user_said = input(f'{user_name} do you want to play Number Guessing game (Y/N) : ').lower()

while True:

    if ('y' not in user_said) and ('n' not in user_said) and (user_said != True):
        user_said = input('Invalid keyword\nType again : ').lower()

    elif 'y' in user_said:
        winning_number = randint(1,100)
        user_guessed = int(input('\nYou have 6 guesses.\nGuess any number between 1 and 100\nGuess the number : '))
        turn = 1

        while True:
        
            if winning_number == user_guessed:
                print(f'Congrats you guessed the number in {turn} times.')
                break

            elif turn == 6:
                print(f'Sorry You can\'t guess the number. The number is {winning_number}.')
                break

            else:
                if winning_number > user_guessed:
                    print('Too Low')
                else:
                    print('Too High')

                print(f'You have {6-turn} guesses left.')
                turn += 1
                user_guessed = int(input('Guess again : '))

        user_said = input(f'\n{user_name} do you want to play more (Y/N) : ')

    else:
        print(f'\nOk Bye {user_name}. See You soon.')
        break
