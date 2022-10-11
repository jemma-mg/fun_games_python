import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = input(f"Guess a number between 1 and {x}: ")
        if guess < random_number:
            print("Sorry guess again, Too Low")
        elif guess > random_number:
            print("Sorry guess again, Too High")
    print(
        f"Yay, congrats you have guessed the number {random_number} correctly!")


def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)  # error if low == high
        else:
            guess = low  # because low = high
        feedback = input(
            f"Is {guess} too high (H), too low (L), or correct (C)?").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f"Yay!, The computer guessed your number, {guess}, correctly!")


# guess(10)
computer_guess(1000)
