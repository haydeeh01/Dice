import random
import time

min = 1
max = 6
done = False
question = input("Type R to roll the dice")
if question.lower() == "r":
    print("Rolling...")
    time.sleep(1)
    print(random.randint(min, max))
    print(random.randint(min, max))
while not done:
    again = input("Would you like to roll again? Y/N")
    if again.lower() == "n":
        print("Goodbye.")
        time.sleep(1)
        done = True
        exit()
    if again.lower() == "y":
        done = False
        print("Rolling...")
        time.sleep(1)
        print(random.randint(min, max))
        print(random.randint(min, max))
