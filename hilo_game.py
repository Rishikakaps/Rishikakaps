high = 1000
low = 1
print('think of a number between {low} and {high}')
input('press enter when you are ready')
guesses = 1 
while True:
    print(f'my guess is {low + (high - low)//2}')
    feedback = input('is it too high (H), too low (L), or correct (C)? ').upper()
    if feedback == 'H':
        high = low + (high - low)//2
        guesses += 1
    elif feedback == 'L':
        low = low + (high - low)//2
        guesses += 1
    elif feedback == 'C':
        print(f'i got it in {guesses} guesses')
        break
    else:
        print('please enter H, L, or C')
        