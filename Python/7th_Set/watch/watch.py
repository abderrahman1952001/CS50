import re

def main():
    html = input("HTML: ")
    print(parse(html))


def parse(string):
    pattern = r'iframe.+src="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]{11})"'
    match = re.search(pattern, string)
    if match:
        return f"https://youtu.be/{match.group(1)}"
    return None



if __name__ == "__main__":
    main()
