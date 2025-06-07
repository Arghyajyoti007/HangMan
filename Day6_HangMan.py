import random
from Day6_Hangman_Stages import stages, logo
from Day6_Hangman_words import word_list
print(logo)

# TODO 1 : Guess a Random Word from the List
lives = 6
selected_word = random.choice(word_list)
# print(selected_word)

# TODO 1.1 : Create a "Placeholder" with the number of blanks as the choosen word
placeholder = ""
for i in range(len(selected_word)):
    placeholder += "_"

print(placeholder)

# TODO 2 : Ask the user to Guess a letter
# TODO 2.1.1 : Add a while loop to give user chance to provide guess again
game_over = False
correct_letters = []


while not game_over:
    print(f"You have : {lives}/6 lives left")
    guess = input("""Guess a Letter : """).lower()
    if guess in correct_letters:
        print(f"You already chose {guess}")

# TODO 3 : Check if the guessed letter is in the Chosen Word
# TODO 3.1 : Create a "Display" that puts the guessed letter in the right position and "_" in the rest of the place
    display = ""

    for letter in selected_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if "_" not in display:
        game_over = True
        print("You Win")
    if guess not in selected_word:
        print(f"You choose {guess}, which is wrong. You lose a life!")
        lives -= 1
        if lives == 0:
            game_over = True
            print(f"It was {selected_word}. You Lose")

    print(stages[lives])


