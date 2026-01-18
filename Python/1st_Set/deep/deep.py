answer = input("What is the answer to the Great Question of Life, the Universe and Everything? ")

match answer.casefold().strip():
    case '42' | 'forty-two' | 'forty two':
        print('yes')
    case _:
        print('No')
