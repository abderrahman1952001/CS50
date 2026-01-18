import inflect

def main():
    names = []
    p = inflect.engine()
    while True:
        try:
            name = input("Name: ").strip()
        except EOFError:
            print()
            break
        names.append(name)

    print(f"Adieu, adieu, to {p.join(names)}")



if __name__ == '__main__':
    main()


