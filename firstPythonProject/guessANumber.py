#Guess a number game
import  random

print('Hello, what is your name?? : ')
name = input()

print('Hello ' + name + ' !. I have in mind a number between 1 and 30')
secretNumber = random.randint(1, 30)

for guessesTaken in range(1, 8):
    print('Please take a guess! :')
    try:
        guess = int(input())

        if guess < secretNumber:
            print('I am thinking about a higher number! Try again!')
        elif guess > secretNumber:
            print('I am thinking about a lower number! Try again! ')
        else:
            break #right guess
    except ValueError:
        print('You did not enter a valid number!')


if guess == secretNumber:
    print('Congrats, ' + name + ' , you have guessed! It took you ' + str(guessesTaken) + ' guesses to win!')
else:
    print('You lose! The number I was thinking of was: ' + str(secretNumber))

