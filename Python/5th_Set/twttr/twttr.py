def main():
    inputed = input("Type a text: ").strip()

    print(shorten(inputed), end="")



def shorten(text):
    stripped_text = []
    vowels = {'a', 'e', 'i', 'o', 'u'}
    for char in text:
        if char.lower() not in vowels:
            stripped_text.append(char)
    return "".join(stripped_text)


if __name__ == "__main__":
    main()
