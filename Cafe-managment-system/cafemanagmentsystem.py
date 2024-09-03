# Define menu of a restaurant

menu = {
    "pizza": 40,
    "pasta": 50,
    "burger": 60,
    "salad": 70,
    "coffee": 80,
    
}

# Greting customer & menu display

print("Welcome to Cafe & Restaurant")
print("pizza: Rs 40\npasta: Rs 50\nburger: Rs 60\nsalad: Rs 70\ncoffee: Rs 80")

order_total = 0

item_1 = input("What do you want to order?\n")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item {item_1} has been add to order.")
else:
    print("Your order is currently not available")

item_2 = input("Do you want any thing else?(yes/no)\n")
if item_2 == "yes":
    another_item = input("Enter your second item = ")
    if another_item in menu:
        order_total += menu[another_item]
        print(f"item {another_item} has been added to you order")
    else:
        print("Order un-available")

print(f"Your order total amount to pay: {order_total}")