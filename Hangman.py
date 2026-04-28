import random

print("🎮 Welcome to Hangman!")

# simple word list
words = ["apple", "tiger", "chair", "robot", "green"]

# choose a random word
word = random.choice(words)

guessed = []
wrong_attempts = 0
max_attempts = 6

# game starts
while wrong_attempts < max_attempts:
    display = ""

    # show current progress
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display.strip())

    # check if completed
    if "_" not in display:
        print("🎉 You guessed the word correctly:", word)
        break

    guess = input("Enter a letter: ").lower()

    # basic validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.")
        continue

    if guess in guessed:
        print("You already tried this letter.")
        continue

    guessed.append(guess)

    if guess in word:
        print("Good guess 👍")
    else:
        wrong_attempts += 1
        print("Wrong guess ❌ | Attempts left:", max_attempts - wrong_attempts)

# losing condition
if wrong_attempts == max_attempts:
    print("\nGame Over! The word was:", word)
