trades = [300, -50, 100, -20]

for profit in trades:
    if profit > 0:
        print(f"WIN ${profit}")
    else:
        print(f"Loss ${profit}")
