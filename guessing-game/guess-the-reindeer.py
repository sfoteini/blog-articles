from random import seed
from random import randrange
from datetime import datetime


seed(datetime.now())
reindeers = ["Blixem", "Comet", "Cupid", "Dancer", "Dasher", "Dunder", "Prancer", "Rudolph", "Vixen"]

print("=== Guess the Santa's Reindeer Name Game ===")
reindeer_name = reindeers[randrange(len(reindeers))]
wrong_answers = 0

while wrong_answers < 3:
    guess = input("What is the name of the reindeer? ").capitalize()

    if guess == reindeer_name:
        print("That's right! It's " + guess)
        print("Merry Christmas!")
        break
    else:
        print("That's wrong!")
        wrong_answers += 1
else:
    print("It's " + reindeer_name)