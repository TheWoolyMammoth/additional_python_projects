############################
# Project: Simple Bisection Search
# Descriptiion: bounds are set to 0 and 100,user inputs an integer between 0 and 100 and then takes
# a guess from the user.
# Date: 08 May, 2021
############################
guess = int(input("Guess a number between 0 and 100: "))
print("Guess:",guess)
low = 0
high = 100
mid = (high+low)//2
count = 0
while True:
    print("Low:",low,"High:",high,"Guess:",mid)
    count += 1
    if guess != mid:
        if guess > mid:
            #guess is higher than original guess
            low = mid
            mid = (high+low)//2
        elif guess < mid:
            #guess is less than original guess
            high = mid
            mid = (high+low)//2
    else:
        print("Guess",mid,"User Value:",guess,"Number of Runs:",count)
        break