months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    year, month, day = get_date()
    print(fix_format(year, month, day))


def get_date():
    while True:
        try:
            date = input("Date: ").strip()

            if '/' in date:
                month, day, year = date.split('/')
                month, day, year = int(month), int(day), int(year)

            elif ',' in date:
                month_day, year = date.split(',')
                month, day = month_day.strip().split()
                day, year = int(day), int(year)

                if month not in months:
                    continue
                month = months.index(month) + 1

            else:
                continue

        except ValueError:
            continue

        if not (1 <= m <= 12 and 1 <= d <= 31):
            continue

        return year, month, day

'''
we can do it like this also:
        if month not in range(1,13):
            continue
        if day not in range(1, 32):
            continue
'''





def fix_format(year, month, day):
    return f"{year}-{month:02d}-{day:02d}"



if __name__ == '__main__':
    main()


