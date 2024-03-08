# Import Dependencies
import random
from hangman_art import stages, logo
from hangman_words import word_list

# Generate a random word from the hangman_words file
chosen_word = random.choice(word_list)
# Save the length of this word in a variable
word_length = len(chosen_word)

# Declare variables needed for control of game
end_of_game = False
lives = 6

# Print it at the start of the game.
print(logo)

# Create by declaring empty list and filling it with blank spaces for each letter in the random word
display = []
for _ in range(word_length):
    display += "_"

# Use while loop to create cycle of game that will break when player has lost all of lives or guessed all the letters in the word
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You've already guessed {guess}")

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            # If letter in word, replace blank space in display with letter
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        # If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        # Decrease life count
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")
    # Display the current hangman art based on amount of lives left
    print(stages[lives])