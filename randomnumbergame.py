import random
number = random.randint(1,15)
guess = int(input('what is your guess? '))
print(number) #todo remove this line
while guess != number:
    if guess < number:
        guess = int(input('guess higher :'))
    elif guess > number:
        guess = int(input('guess lower :'))
    elif guess == number:
        print('you got it!')
        break

print('you are correct!')
    