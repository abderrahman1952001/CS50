
def convert(sentence):
    return sentence.replace(':)', '🙂').replace(':(', '🙁')

def main():
    word = input("Type something with emoticons: ")
    print(convert(word))


main()

