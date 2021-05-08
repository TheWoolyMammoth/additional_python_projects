############################
# Project: Set Simple Bisection Search
# Descriptiion: set the bounds of your search (upper and lower), and then takes
# a guess from the user.
# Date: 08 May, 2021
############################

lower_bound = int(input("Enter an Lower Bound: "))
upper_bound = int(input("Enter an Uppper Bound: "))
user_value = int(input("Enter your guess: "))
count=0

while True:
    guess = (upper_bound+lower_bound)//2
    count+=1
    if guess == user_value:
        print("User Value ",user_value)
        print("Number of Runs ",count)
        break
    if guess < user_value:
        lower_bound = guess
        print("Too Low - Lower:",lower_bound,"Upper:",upper_bound,"Guess",guess)
    elif guess >user_value:
        upper_bound=guess
        print("Too High - Lower:", lower_bound, "Upper:", upper_bound, "Guess", guess)
    if lower_bound == upper_bound:
        print("Failure.")
        break
