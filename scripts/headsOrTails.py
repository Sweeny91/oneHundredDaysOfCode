import random

choice = input("Do you pick heads or tails? (h/t) ")
## could print the results to the screen here
result = random.randint(0,1)
## and again here for 'result'

# control for choice int in the instance the user doesnt input h or t
choiceint = 3

if choice == 'h':
    choiceint = 0
elif choice == 't':
    choiceint = 1

if (choiceint == 1 or choiceint == 0):
    if choiceint == result:
        print("\nYou got it!")
    else:
        print("\nNope, wrong choice!")
else:
    print("Invalid Entry. Try again.")