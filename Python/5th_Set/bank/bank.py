def main():
    greeting = input("Greeting: ").lstrip().casefold()
    print(f"${value(greeting)}")


def value(greeting):
    if greeting[0] == 'h':
        return 0 if greeting[:5] == 'hello' else return 20
    else:
        return 100



if __name__ == "__main__":
    main()
