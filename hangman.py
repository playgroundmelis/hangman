"""
Hangman: A standard game of Hangman.
A word is chosen at random from a list and the
user must guess the word letter by letter before running out of attempts.
"""

import random

def main():
    welcome_message = [
        "Welcome to Hangman! 🎩✨",
        "A word will be chosen at random, and",
        "you must try to guess the word correctly letter by letter",
        "before you run out of attempts. Good luck! 🍀"
    ]

    for line in welcome_message:
        print(line)

    play_again = True

    while play_again:
        words = ["hangman", "chairs", "backpack", "bodywash", "clothing",
                 "computer", "python", "program", "glasses", "sweatshirt",
                 "sweatpants", "mattress", "friends", "clocks", "biology",
                 "algebra", "suitcase", "knives", "ninjas", "shampoo", "house", 
                 "cat", "dog", "tree", "car", "book", "computer", "phone", "table", 
                 "chair", "water", "food", "love", "friend", "work", "time", "money",
                 "music", "movie", "family", "school", "city", "country", "sky", "sun", 
                 "moon", "star", "flower", "garden", "beach", "mountain", "river", "lake", 
                 "ocean", "rain", "snow", "wind", "cloud", "fire", "earth", "air", "life", 
                 "heart", "mind", "body", "dream", "hope", "faith", "joy", "peace", 
                 "health", "happiness", "success", "challenge", "change", "growth", "journey", 
                 "experience", "memory", "imagination", "creativity", "passion", "purpose", 
                 "inspiration", "motivation", "achievement", "victory", "failure", 
                 "fear", "courage", "confidence", "belief", "trust", "kindness", 
                 "generosity", "compassion", "gratitude", "patience", "forgiveness", 
                 "understanding", "empathy", "communication", "connection", "relationship", 
                 "bond", "love", "friendship", "family", "community", "society", "world", "universe"
                 ]

        chosen_word = random.choice(words).lower()
        player_guess = None 
        guessed_letters = [] 
        word_guessed = ["-" for _ in chosen_word] 

        HANGMAN = (
            """
            -----
            |   |
            |
            |
            |
            |
            |
            |
            |
            --------
            """,
            """
            -----
            |   |
            |   0
            |
            |
            |
            |
            |
            |
            --------
            """,
            """
            -----
            |   |
            |   0
            |  -+-
            |
            |
            |
            |
            |
            --------
            """,
            """
            -----
            |   |
            |   0
            | /-+-
            |
            |
            |
            |
            |
            --------
            """,
            """
            -----
            |   |
            |   0
            | /-+-\ 
            |
            |
            |
            |
            |
            --------
            """,
            """
            -----
            |   |
            |   0
            | /-+-\ 
            |   | 
            |
            |
            |
            |
            --------
            """,
            """
            -----
            |   |
            |   0
            | /-+-\ 
            |   | 
            |   | 
            |
            |
            |
            --------
            """,
            """
            -----
            |   |
            |   0
            | /-+-\ 
            |   | 
            |   | 
            |  |
            |
            |
            --------
            """,
            """
            -----
            |   |
            |   0
            | /-+-\ 
            |   | 
            |   | 
            |  | 
            |  | 
            |
            --------
            """,
            """
            -----
            |   |
            |   0
            | /-+-\ 
            |   | 
            |   | 
            |  | | 
            |  | 
            |
            --------
            """,
            """
            -----
            |   |
            |   0
            | /-+-\ 
            |   | 
            |   | 
            |  | | 
            |  | | 
            |
            --------
            """
        )

        print(HANGMAN[0])
        attempts = len(HANGMAN) - 1

        while attempts != 0 and "-" in word_guessed:
            print(f"\nYou have {attempts} attempts remaining")
            print("".join(word_guessed))

            try:
                player_guess = input("\nPlease select a letter between A-Z\n> ").lower()
            except:
                print("Umm, you know that's not a letter, right? Try again lol.")
                continue                
            else: 
                if not player_guess.isalpha():
                    print("Umm, you know that's not a letter, right? Try again lol.")
                    continue
                elif len(player_guess) > 1:
                    print("Umm, you know that's more than one letter, right? Try again lol.")
                    continue
                elif player_guess in guessed_letters:
                    print("You already guessed that one, brooks :) Try again.")
                    continue

            guessed_letters.append(player_guess)

            for index, letter in enumerate(chosen_word):
                if player_guess == letter:
                    word_guessed[index] = player_guess

            if player_guess not in chosen_word:
                attempts -= 1
                print(HANGMAN[len(HANGMAN) - attempts])

        if "-" not in word_guessed:
            print(f"\nCongratulations! '{chosen_word}' was the word.")
        else:
            print(f"\nUnlucky! The word was '{chosen_word}'.")

        print("\nWould you like to play again?")

        response = input("> ").lower()
        if response not in ("yes", "y"):
            play_again = False

if __name__ == "__main__":
    main()
