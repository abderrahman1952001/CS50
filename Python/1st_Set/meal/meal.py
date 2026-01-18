def main():
    Time = convert(input("Type the time: ").strip())

    if 7 <= Time <= 8:
        print("breakfast time")
    elif 12 <= Time <= 13:
        print("lunch time")
    elif 18 <= Time <= 19:
        print("dinner time")



def convert(time_as_string):
    time , *rest = time_as_string.split(maxsplit=1)
    format = rest[0] if rest else None

#OR:
# time , format = (time_as_string.split(maxsplit=1) + [None])[:2]

    h , min = time.split(":")
    h , min = float(h) , float(min)
    time = h + (min / 60)

    # Optional 12-hour support
    if format in ("a.m.", "p.m."):
        if format == "p.m.":
            time += 12

    return time




if __name__ == "__main__":
    main()
