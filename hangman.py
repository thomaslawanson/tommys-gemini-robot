import random
import os

words = [
    "apple", "grape", "peach", "mango", "berry", "melon", "tiger", "zebra", "chair", "table",
    "sofa", "house", "pencil", "flower", "grass", "cloud", "smile", "laugh", "write", "dance",
    "happy", "brown", "green", "black", "yellow", "orange", "train", "plane", "truck", "bread",
    "cheese", "pizza", "pasta", "fruit", "chalk", "board", "water", "river", "ocean", "beach",
    "school", "teacher", "rabbit", "donkey", "monkey", "banana", "basket", "forest", "bridge",
    "castle", "island", "saddle", "pirate", "rocket", "helmet", "bottle", "laptop", "window",
    "pillow", "sugar", "cookie", "spoon", "honey", "butter", "candle", "basket", "garden",
    "puzzle", "planet", "camera", "rocket", "sunset", "sunny", "storm", "turtle", "kitten",
    "puppy", "cattle", "donut", "silver", "buzzer", "ticket", "jungle", "helmet", "ladder",
    "stream", "campus", "cactus", "potato", "tomato", "pepper", "copper", "cherry", "gravel"
]

HANGMAN_PICS = [
    """
       ------
       |    |
       |
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    --------
    """
]

def get_hints(word, guessed_letters):
    word_length = len(word)
    for _ in range(3):
        random_index = random.randint(0, word_length - 1)
        guessed_letters.append(word[random_index])

def update_mask(word_mask, guessed_letters, letters_list):
    for letter in guessed_letters:
        for i, char in enumerate(letters_list):
            if char == letter and word_mask[i] == "_":
                word_mask[i] = letter
                return " ".join(word_mask)
    return " ".join(word_mask)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_game(wrong_attempts, visible_word):
    clear_screen()
    print(HANGMAN_PICS[wrong_attempts])
    print('Word:', visible_word)
    print("Wrong Attempts:", wrong_attempts)

def play_hangman():
    word = random.choice(words)
    letters_list = list(word)
    guessed_letters = []
    word_mask = ['_'] * len(letters_list)
    wrong_attempts = 0
    max_attempts = len(HANGMAN_PICS) - 1
    visible_word = " ".join(word_mask)
    get_hints(word, guessed_letters)
    for _ in range(3):
        visible_word = update_mask(word_mask, guessed_letters, letters_list)
    while wrong_attempts < max_attempts:
        visible_word = update_mask(word_mask, guessed_letters, letters_list)
        display_game(wrong_attempts, visible_word)
        user_input = input("Guess a letter: ").lower()
        if len(user_input) != 1 or not user_input.isalpha():
            print("Invalid input. Please enter a single letter.")
            input("\nPress Enter to continue")
            continue
        if user_input in guessed_letters:
            print("You already guessed that letter!")
            input("\nPress Enter to continue")
            continue
        guessed_letters.append(user_input)
        if user_input in letters_list:
            print("Correct!")
            visible_word = update_mask(word_mask, guessed_letters, letters_list)
            if "_" not in visible_word:
                display_game(wrong_attempts, visible_word)
                print("You WON the game!")
                return
        else:
            print("Wrong guess.")
            wrong_attempts += 1
    display_game(wrong_attempts, visible_word)
    print("You lost the game. The word was:", word)

if __name__ == "__main__":
    play_hangman()
