import json
import random
import datetime

current_time = datetime.datetime.now()

print(current_time)

secret = random.randint(1, 30)
attempts = 0

with open("score_list.txt", "r") as score_file:
    score_list = json.loads(score_file.read())    # pretvara string u list i sprema u varijablu score_list
    # print("Top scores: " + str(score_list))

    for score_dict in score_list:
        print(str(score_dict["attempts"]) + " attempts, name: " + score_dict.get("ime") + ", date: " +
              score_dict.get("date") + ", secret number: " + str(score_dict["broj"]))

ime = input("Upiši svoje ime: ")

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        score_list.append({"attempts": attempts, "date": str(datetime.datetime.now()), "ime": ime, "broj": secret})

        with open("score_list.txt", "w") as score_file:
            """ otvara .txt kao score file i u njega upisuje list 'score_list' te ga pomoću jsona vraća u string """
            score_file.write(json.dumps(score_list))

        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")
