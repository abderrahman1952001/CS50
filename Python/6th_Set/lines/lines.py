import sys

if len(sys.argv) != 2:
    sys.exit("Too few command-line arguments") if len(sys.argv) <2 else sys.exit("Too many command-line arguments")

filename = sys.argv[1]

if not filename.endswith(".py"):
    sys.exit("Not a Python file")

count = 0

try:
    with open(filename) as file:
        for line in file:
            if line.lstrip() == "" or line.strip()[0] == "#":    #we can use line.startswith("#")
                continue
            count +=1

except FileNotFoundError:
    sys.exit("File does not exist")


print(count)
