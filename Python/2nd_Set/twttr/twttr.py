def vowel_remover(text):
    stripped_text = []
    vowels = {'a', 'e', 'i', 'o', 'u'}
    for char in text:
        if char.casefold() not in vowels:
            stripped_text.append(char)
    return "".join(stripped_text)

inputed = input("Type a text: ").strip()

print(vowel_remover(inputed), end="")
