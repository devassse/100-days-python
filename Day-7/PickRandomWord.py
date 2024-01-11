#Pick the word from the LIST
import random
print("Guess The Word! Inter QUIT to exit Game")

words = ["Manga", "Pa", "Cabelo"]


user_word = ""
spaces = []
while user_word != "QUIT":

    word = random.choice(words)
    word_size = len(word)

    for i in range(word_size):
        spaces.append("_")

    print(spaces)
    spaces.clear()

    user_word = input("Guess what is the Word!? ")

    if word == user_word:
        print("Congrats, you guessed")
    else:
        print("Wrong, try again ...")


