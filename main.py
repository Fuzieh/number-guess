import random


number = random.randint(10, 99)
tries = 0

while tries <= 3:
    if tries == 3:
        print(f"Correct answer is: {number} \n Bye Bye :))")
        break
    tries += 1
    user_guess = input("Enter your guess: ")
    if user_guess.isdigit():
        if int(user_guess) == number:
            print("You win! :)")
            break
        else:
            if number > int(user_guess):
                print("Enter greater number")
            else:
                print("Enter lesser number")
            continue
    else:
        print("Invalid number")
        continue


