items = {}


def main():
    while True:
        try:
            item = input()
        except EOFError:
            break

        items[item]= items.get(item, 0) + 1

    for item in sorted(items):
        print(items[item], item.upper())


if __name__ == "__main__":
    main()
