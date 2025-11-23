
print("=========== COLLEGE STATIONERY SHOP ===========")

# items and their prices (I added what we usually buy in college)
items = {
    1: ("Pencil", 4),
    2: ("Pen", 5),
    3: ("Notebook", 40),
    4: ("Eraser", 3),
    5: ("Sharpener", 5),
    6: ("Highlighter", 25),
    7: ("Geometry Box", 60),
    8: ("Paper Sheets", 2),
    9: ("Stapler", 35),
    10: ("Markers", 20),
    11: ("Glue Bottle", 15),
    12: ("Sticky Notes", 10)
}

total = 0
bill = []

while True:
    print("\n------ AVAILABLE ITEMS ------")
    for i in items:
        # showing item id, name and price
        print(i, items[i][0], "- Rs", items[i][1])

    try:
        item_no = int(input("\nEnter item number you want to buy: "))
    except:
        print("Please enter a number only.")
        continue

    if item_no not in items:
        print("Invalid choice... try again.")
        continue

    name, price = items[item_no]

    # asking quantity
    qty = int(input(f"How many {name} do you want? "))

    amt = qty * price
    total += amt
    bill.append((name, qty, amt))

    print(name, "added to cart! Amount =", amt)

    # asking if student wants more
    more = input("Buy anything else? (yes/no): ")
    if more.lower() != "yes":
        break

# final bill
print("\n============== FINAL BILL ==============")
for item in bill:
    print(item[0], "x", item[1], "=", item[2])

print("-----------------------------------------")
print("Total Amount to Pay: Rs", total)
print("Thank you!")