# Write your code here
import random

l = ['python', 'java', 'kotlin', 'javascript']
sel = random.choice(l)

hidden = ["-" for i, _ in enumerate(sel)]
chars = []
tries = 8

print("H A N G M A N")
while tries > 0:
    tries -= 1
    print("")
    print("".join(hidden))
    ch = input("Input a letter: ")
    if ch in sel:
        for i, c in enumerate(sel):
            if ch == c:
                hidden[i] = ch

    else:
        print("No such letter in the word")
print("")
print("Thanks for playing!")
print("We'll see how well you did in the next stage")




