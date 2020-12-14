# Write your code here
from random import choice
rating = 0
name = input("Enter your name: ")
print("Hello, " + name)
with open("rating.txt", 'r') as f:
    lines = f.readlines()
    for x in lines:
        if x.split()[0] == name:
            rating = int(x.split()[1])
options = input()
if options == "":
    valid = ["rock", "paper", "scissors"]
else:
    valid = options.split(',')
print("Okay, let's start")
while True:
    c = choice(valid)
    p = input()
    if p == "!exit":
        print("Bye!")
        exit()
    elif p == "!rating":
        print("Your rating: {}".format(rating))
    elif p in valid:
        if p == c:
            print("There is a draw ({})".format(c))
            rating += 50
        else:
            loses = set()
            i = valid.index(p)
            l = len(valid)
            m = int((l - 1) / 2)
            for n in range(1, m + 1):
                if i + n >= l:
                    loses.add(valid[i + n - l])
                else:
                    loses.add(valid[i + n])
            if c in loses:
                print("Sorry, but the computer chose {}".format(c))
            else:
                print("Well done. The computer chose {} and failed".format(c))
                rating += 100
    else:
        print("Invalid input")
