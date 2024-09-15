# Products available in the store by category

products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15),
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450),
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8),
    ],
}

cart = []


def display_sorted_products(products_list, sort_order):
    if sort_order == "asc":
        products_list = sorted(products_list, key=lambda x: x[1], reverse=False)
    elif sort_order == "desc":
        products_list = sorted(products_list, key=lambda x: x[1], reverse=True)
    for x in products_list:
        print(x)
    return products_list


def display_products(products_list):
    for x, y in products_list:
        print(f"{x}: {y}")


'''def display_categories():
    print("Product Categories")
    num = 1
    for key in products:
        print(f"{num}. {key}")
        num += 1'''

def display_categories():
    print("Product Categories")
    num = 1
    categories = list(products.keys())
    for key in categories:
        print(f"{num}. {key}")
        num += 1

    try:
        choice = int(input("Please select a category by number (or 0 to exit): "))
        if 1 <= choice <= len(categories):
            return choice - 1  # 返回索引（从0开始）
        else:
            return None  # 输入无效或用户选择退出
    except ValueError:
        return None  # 如果输入不是数字，返回None


def add_to_cart(cart, product, quantity):
    item = (product[0], product[1], quantity)
    cart.append(item)
    print(
        f"{quantity} {product[0]}(s) priced at {product[1]} have been added to your cart."
    )
    print(cart)


def display_cart(cart):
    total_cost = 0
    for item in cart:
        product_name, price, quantity = item
        item_total = price * quantity
        total_cost += item_total
        print(f"{product_name} - ${price} x {quantity} = ${item_total}")

    print(f"Total cost: ${total_cost}")
    return total_cost


def generate_receipt(name, email, cart, total_cost, address):
    receipt = f"--- Receipt ---\n"
    receipt += f"Name: {name}\n"
    receipt += f"Email: {email}\n"
    receipt += f"Address: {address}\n\n"
    receipt += "Items purchased:\n"

    for item in cart:
        product_name, price, quantity = item
        item_total = price * quantity
        receipt += f"{product_name} - ${price} x {quantity} = ${item_total}\n"

    receipt += f"\nTotal cost: ${total_cost}\n"
    receipt += f"Thank you for shopping with us!"

    return receipt


def validate_name(name):
    part = name.split()
    if len(part) != 2:
        return False
    part1, part2 = part
    if part1.isalpha() and part2.isalpha():
        return True
    else:
        return False


def validate_email(email):
    flag = False
    for x in email:
        if x == "@":
            flag = True
    return flag

    # return True if "@" in email and "." in email.split("@")[-1] return False


# This function handles category selection and product interaction.
def category_selection(name, email):
    display_categories()

    choice = int(input("Which category you would like to explore?"))
    while True:
        if choice == 1:
            display_products(products["IT Products"])
            break
        elif choice == 2:
            display_products(products["Electronics"])
            break
        elif choice == 3:
            display_products(products["Groceries"])
            break
        else:
            print("Input invalid! Try again!")
            choice = int(input("Which category you would like to explore?"))

    product_interaction(name, email, choice)


# This function handles product selection, sorting, and the cart process.
def product_interaction(name, email, choice):
    print("Now choose what you need:")
    print("1. Select a product to buy")
    print("2. Sort the products according to the price")
    print("3. Go back to the category selection")
    print("4. Finish shopping")

    choice_need = int(input("Which you would like to explore?"))
    while True:
        if choice_need == 1:
            product_parts = (input("Product: ")).rsplit(" ", 1)
            product_name = product_parts[0]
            product_price = int(product_parts[1])
            product = (product_name, product_price)
            quantity = int(input("Quantity:"))
            add_to_cart(cart, product, quantity)
            choice_need = int(input("Which you would like to explore?"))

        elif choice_need == 2:
            order = int(input("Do you want to sort ascending (1) or descending (2)?"))
            while order != 1 and order != 2:
                order = int(
                    input(
                        "Input invalid! Try again! Do you want to sort ascending (1) or descending (2)?"
                    )
                )

            if order == 1:
                order = "asc"
            elif order == 2:
                order = "desc"

            if choice == 1:
                display_sorted_products(products["IT Products"], order)
            elif choice == 2:
                display_sorted_products(products["Electronics"], order)
            elif choice == 3:
                display_sorted_products(products["Groceries"], order)

            choice_need = int(input("Which you would like to explore?"))

        elif choice_need == 3:
            # Call category_selection again to go back to category choice
            category_selection(name, email)
            break

        elif choice_need == 4:
            if cart:
                print(cart)
                total_cost = display_cart(cart)
                address = input("Please give me your address:")
                print(
                    "The order will be delivered in 3 days, and the payment will be charged after the delivery is successful."
                )
                print("Here is the receipt:")
                receipts = generate_receipt(name, email, cart, total_cost, address)
                print(receipts)
            else:
                print(
                    "Thank you for using our portal. Hope you buy something from us next time. Have a nice day!"
                )
            break
        else:
            print("Input invalid! Try again!")
            choice_need = int(input("Which you would like to explore?"))


# Main function to start the shopping process.
def main():
    print("Welcome to Online Shopping Store")

    name = input("Please give me your name:")
    while not validate_name(name):
        name = input("Input invalid! Please give me your name:")

    email = input("Please give me your email:")
    while not validate_email(email):
        email = input("Input invalid! Please give me your email:")

    category_selection(name, email)


"""def main():
    print("Welcome to Online Shopping Store")

    name = input("Please give me your name:")
    while True:
        if validate_name(name):
            break
        else:
            name = input("Input invalid! Please give me your name:")

    email = input("Please give me your email:")
    while True:
        if validate_email(email):
            break
        else:
            email = input("Input invalid! Please give me your email:")

    display_categories()

    choice = int(input("Which category you would like to explore?"))
    while True:
        if choice == 1:
            display_products(products["IT Products"])
            break
        elif choice == 2:
            display_products(products["Electronics"])
            break
        elif choice == 3:
            display_products(products["Groceries"])
            break
        else:
            print("Input invalid! Try again!")

    print("Now choose what you need:")
    print("1. Select a product to buy")
    print("2. Sort the products according to the price")
    print("3. Go back to the category selection")
    print("4. Finish shopping")

    choice_need = int(input("Which you would like to explore?"))
    while True:
        if choice_need == 1:
            product_parts = (input("Product: ")).rsplit(' ', 1) 
            product_name = product_parts[0]  
            product_price = int(product_parts[1])  
            product = (product_name, product_price)  
            quantity = int(input("Quantity:"))
            add_to_cart(cart, product, quantity)
            choice_need = int(input("Which you would like to explore?"))

        elif choice_need == 2:
            order = int(input("Do you want to sort ascending (1) or descending (2)?"))
            while True:
                if order == 1 or order == 2:
                    break
                else:
                    order = int(input("Input invalid! Try again! Do you want to sort ascending (1) or descending (2)?"))
            
            if order == 1:
                order = "asc"
            elif order == 2:
                order = "desc"

            if choice == 1:
                display_sorted_products(products["IT Products"], order)
            elif choice == 2:
                display_sorted_products(products["Electronics"], order)
            elif choice == 3:
                display_sorted_products(products["Groceries"], order)
            choice_need = int(input("Which you would like to explore?"))

        elif choice_need == 3:
            #go back
            break

        elif choice_need == 4:
            if cart != None:
                print(cart)
                total_cost = display_cart(cart)
                address = input("Please give me your address:")
                print("The order will be delivered in 3 days, and the payment will be charged after the delivery is successful.")
                print("Here is the receipt:")
                receipts = generate_receipt(name, email, cart, total_cost, address)
                print(receipts)
            else:
                print("Thank you for using our portal. Hope you buy something from us next time. Have a nice day!")

            break
        else:
            print("Input invalid! Try again!")"""


""" The following block makes sure that the main() function is called when the program is run. 
It also checks that this is the module that's being run directly, and not being used as a module in some other program. 
In that case, only the part that's needed will be executed and not the entire program """
if __name__ == "__main__":
    main()
