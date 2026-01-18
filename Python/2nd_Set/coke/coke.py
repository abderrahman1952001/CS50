due = 50

valid_coins = {5, 10, 25}

while due > 0:
    print("Amount due:", due)
    coin = int(input("Insert Coin: "))
    if coin in valid_coins:
        due -= coin

print("Change Owed:", -due)




