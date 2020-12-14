# Write your code here
from random import choice

print("H A N G M A N")
words = ['python', 'java', 'kotlin', 'javascript']
while True:
    play = ""
    while play != "play" or play != "exit":
        play = input('Type "play" to play the game, "exit" to quit:')
        if play == "exit":
            exit()
        elif play == "play":
            right_word = choice(words)
            guess = "-"*len(right_word)
            guessed = set()
            tries = 8
            while tries > 0:
                print("\n"+guess)
                char = input("Input a letter:")
                if len(char) != 1:
                    print("You should input a single letter")
                elif char not in "abcdefghijklmnopqrstuvwxyz":
                    print("Please enter a lowercase English letter")
                elif char in right_word and char not in guess:
                    guessed.add(char)
                    guess = "".join([x if x in guessed else "-" for x in right_word])
                elif char in guessed and char != "":
                    print("You've already guessed this letter")
                else:
                    print("That letter doesn't appear in the word")
                    tries -= 1
                if guess == right_word:
                    print("You guessed the word!\nYou survived!")
                    break
                guessed.add(char)
            if tries == 0:
                print("You lost!\n")
