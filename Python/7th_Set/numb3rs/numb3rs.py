import re


def main():
    ip = input("IPv4 Address: ")
    print(validate(ip))


def validate(ip):
    pattern = r"^(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}$"    #the pattern is: (octet)(\.(octet)){3}
    return bool(re.search(pattern, ip))


def validate_without_regex(ip):
    octets = ip.split(".")

    if len(octets) != 4:
        return False

    for octet in octets:
        if not octet.isdigit():
            return False
        if int(octet) > 255:
            return False
        if len(octet) > 1 and octet.startswith("0"):
            return False

    return True




if __name__ == "__main__":
    main()
