import random
from hangman_art import stages, logo
from hangman_words import word_list


lives = 6

print(logo)

chosen_word = random.choice(word_list)
print(chosen_word)

# Create a "placeholder" with the same number of blanks as the chosen_word
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

# Use a while loop to let the user guess again. 

game_over = False
correct_letters = []

while not game_over:

    print(F"******************<???>/ {lives} LIVES LEFT ******************")

    guess = input("Guess a letter: ").lower()

    # If the user has entered a letter they've already guessed, print the letter and let them know 
    if guess in correct_letters:
        print(f"You have already guessed {guess}")

    display = ""



    # Change the for loop so that you keep the previous correct 

    for letter in chosen_word:
        if letter == guess:
            # if player guesses the correct letter, it is displayed
            display += letter
            # guessed corrected letter are are added onto correct_letter list
            correct_letters.append(guess)
        # if letters are in the 'correct_letter' list, it is shown on display
        elif letter in correct_letters: 
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in display:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print(f"**************** YOU LOSE. THE CORRECT WORD WAS {chosen_word} ****************")

    if "_" not in display:
        game_over = True 
        print(f"**************** YOU WIN. THE CORRECT WORD WAS {chosen_word} ****************")

    print(stages[lives])