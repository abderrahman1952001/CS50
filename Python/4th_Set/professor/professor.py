import random


def main():
    level = get_level()

    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)

        tries = 0

        while tries <3:
            try:
                answer = int(input(f"{x} + {y} = "))
            except ValueError:
                print('EEE')
                tries += 1
                continue

            if answer == x + y:
                score +=1
                break

            print('EEE')
            tries += 1

        if tries == 3:
            print(f"{x} + {y} = {x + y}")

    print(f"Score: {score}")



def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            continue

        if level in range(1,4):
            return level



def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    if level == 2:
        return random.randint(10, 99)
    if level == 3:
        return random.randint(100, 999)
    raise ValueError

'''
def generate_integer(level):
    pairs = []

    if level == 1:
        start, end = 0, 10
    elif level == 2:
        start, end = 10, 100
    elif level == 3:
        start, end = 100, 1000

    for _ in range(10):
        x = random.randrange(start, end)
        y = random.randrange(start, end)
        pairs.append((x, y))

    return pairs

'''


if __name__ == "__main__":
    main()
