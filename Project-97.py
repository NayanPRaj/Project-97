import random
n=random.randint(1,9)
g1=input("Enter your first guess")
if(g1!=n):
    print("Your guess is incorrect. Guess a number higher  than ",g1)
else:
    print("Your guess is correct !! Congratulations")
g2=input("Enter your second guess")
if(g2!=n):
    print("Your guess is incorrect. Guess a number higher  than ",g2)
else:
    print("Your guess is correct !! Congratulations")
g3=input("Enter you third guess")
if(g3!=n):
    print("Your guess is incorrect. Guess a number higher  than ",g3)
else:
    print("Your guess is correct !! Congratulations")
g4=input("Enter your fourth guess")
if(g4!=n):
    print("Your guess is incorrect. Guess a number higher  than ",g4)
else:
    print("Your guess is correct !! Congratulations")
g5=input("Enter your fifth guess")
if(g5!=n):
    print("Your guess is incorrect. Guess a number higher  than ",g5)
else:
    print("Your guess is correct !! Congratulations")
if(g5!=n):
    print("You lose!! The number is",n)

