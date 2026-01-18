import random


def main():
    level = get_level()
    target = generate_number(level)
    guess_number(target)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            continue

        if level >= 1:
            return level


def generate_number(n):
    return random.randint(1, n)

def guess_number(n):
    while True:
        try:
            guess = int(input("Guess: "))
        except ValueError:
            continue

        if guess < 1:
            continue

        if guess < n:
            print("Too small!")
        elif guess > n:
            print("Too large!")
        else:
            print("Just right!")
            break




if __name__ == '__main__':
    main()
