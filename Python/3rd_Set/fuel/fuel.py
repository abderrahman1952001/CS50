def main():
    percentage = get_percentage()
    print(gauge(percentage))


def get_percentage():
    while True:
        fraction = input("Fraction: ")
        try:
            x, operator, y = fraction.partition('/')
            x , y = int(x), int(y)
            if x > y or x < 0 or operator != '/':
                raise ValueError
            else:
                return round(x / y * 100)
                break
        except (ValueError, ZeroDivisionError):
            continue


def gauge(percent):
    if percent >= 99:
        return "F"
    elif percent <= 1:
        return "E"
    else:
        return f"{percent}%"

if __name__ == "__main__":
    main()

