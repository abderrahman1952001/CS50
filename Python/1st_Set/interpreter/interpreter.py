expression = input("Type a math expression: ").strip()

x , o , y = expression.split()

x , y = float(x), float(y)

match o:
    case '+':
        print(x + y)
    case '-':
        print(x - y)
    case '*':
        print(x * y)
    case  '/':
    print(x / y) if y != 0 else print("you can't devide by 0")
else:
    print("invalid expression")



