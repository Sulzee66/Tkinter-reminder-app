import random as rd
unknown = rd.randint(0, 10)
tries=5

while tries> 0:
    guess=int(input('Your guess:\n'))
    if guess==unknown:
        print("Right guess")
        break
    elif guess < unknown:
        print("Try higher number")
    elif guess > unknown:
        print("Try lower number")
    tries-=1
    if tries == 0:
        print("You are out of tries😂")
print("The number you were trying to guess is ",unknown)
