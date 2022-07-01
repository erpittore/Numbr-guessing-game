import random

num = random.randint(0,25)
guess = None

while guess != num:
    guess = input('Guess a number between 0 and 20: ')
    guess = int(guess)

    if guess == num:
        print('Congratulations! You are a winner!!')
        break
    elif guess > num:
        print(f'{guess} is greater.')
    elif guess < num:
        print(f'{guess} is smaller.')
    #else:
       # print('I am sorry please guess again! ')
        #else statement no longer needed after I added in the elif's
