
import random

#Get Guesses
def get_guess():
    return str(input("Hint What is your guess? "))


#Generate Computer random 3 digit code

code = str(random.randrange(100,999))


#Generate Clues
def generate_clues(code,guess):
    print(code)
    print(type(code))
    print(guess)
    print(type(guess))

    if code == guess:
        print("cracked")
        return "CODE CRACKED!"

    clues = []

    for ind,num in enumerate(guess):
        if num == code[ind]:
            clues.append("match")
        elif num in code:
            clues.append("close")
    if clues ==[]:
        return ["NOPE"]
    else:
        return clues


#Game Logic

print("welcome Gamer!")

# code = generate_code()
print(code)


clue_report = []

while clue_report != "CODE CRACKED!":

    guess = get_guess()
    clue_report = generate_clues(code,guess)
    print("This is how you're fairing..")
    for clue in clue_report:
        print(clue)


# x = get_guess()
# print(type(x))
# print(x[0])
# y = generate_code()
# print(y)
