

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")



def is_valid(string):
    return condition1(string) and condition2(string) and condition3(string) and condition4(string)


def condition1(string):
    return string[:2].isalpha()

def condition2(string):
    return 2 <= len(string) <= 6

def condition3(string):
    for position, char in enumerate(string):
        if char.isdigit():
            if char == '0':
                return False
            else:
                return string[position:].isdigit()
    return True


def condition4(string):
    return string.isalnum()



if __name__ == "__main__":
    main()
