greeting = input("Greeting: ").lstrip().casefold()

if greeting[0] == 'h':
    print('$0') if greeting[:5] == 'hello' else print('$20')
else:
    print('$100')


'''
if greeting.startswith("hello"):
    print("$0")
elif greeting.startswith("h"):
    print("$20")
else:
    print("$100")

 this handles an empty input
'''
