import random

secret = random.randint(1,10)
temp = input("guess the number")
guess = int(temp)
count = 1
while (guess != secret)and(count<3):
    if guess > secret:
        print('bigger than number')
    else:
        print('smaller than number')

    temp = input("input again")
    guess = int(temp)
    count = count + 1
    if guess == secret:
        print("bingo!")

if count == 3:
    print('You only have three chances')

print("Game over")
