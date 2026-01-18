
def snake_case(variable):
    output = []
    for char in variable:
        if char.isupper():
            output.append('_' + char.lower())
        else:
            output.append(char)
    return "".join(output)

camel_case = input("camelCase: ")

print(snake_case(camel_case))










