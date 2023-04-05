Secret_word = "Goondy"
guess = ""
Guess_count = 0
Guess_limit = 3
Out_of_guesses = False

while guess != Secret_word and not Out_of_guesses:
    if Guess_count < Guess_limit:
        guess = input("Input Your Guess  : ")
        Guess_count += 1
    else:
        Out_of_guesses = True

if Out_of_guesses:
    print("you lose")
else:
    print("you win")
