

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
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}


def validate_name(name):
    try:
        first_name, last_name = name.strip().split(" ",1)
        if not first_name.isalpha():
            print("your name %s is not contain only alphabets,plz retry"%(first_name))
            return False
        if not last_name.isalpha(): 
            print("your name %s is not contain only alphabets,plz retry"%(last_name))
            return False
        print("first_name:%s, last_name:%s"%(first_name,last_name))
        return True
    except:
        return False
    

def validate_email(email):
    return '@' in email




def display_products(products_list):
    while True:
        try:
            wanna = input("Enter the category number: ")
            if wanna.isdigit():
                wanna = int(wanna)
                if 0 < wanna <= len(products_list):
                    category = products_list[wanna - 1]
                    print(f"\nProducts in '{category}':")
                    product_list = []
                    for index, (product, price) in enumerate(products[category]):
                        product_list.append((index, product, price))
                        print(f"{index + 1}. Product: {product}, Price: ${price}")
                    return product_list
                else:
                    print("Invalid category number, please retry.")
            else:
                print("Invalid input. Please enter a number.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def display_categories():
    print("Now showing the categories:\n")
    categories_list = list(products.keys())
    for index, category in enumerate(categories_list):
        print(f"{index + 1}: {category}")
    
    try:
        wanna = int(input("Enter the category number: "))
        if 0 < wanna <= len(categories_list):
            return wanna - 1
        else:
            print("Invalid category number, please retry.")
            return None
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None



def add_to_cart(cart, product, quantity):
    if isinstance(quantity, int) and quantity > 0:
        cart.append((product[0], product[1], quantity))
        print("Successfully added to cart!")
        for index, item in enumerate(cart):
            product_name = item[0]
            price = item[1]
            quantity = item[2]
            print(f"{index + 1}. Product: {product_name}, Price: ${price}, Quantity: {quantity}")
    else:
        print("Invalid quantity. Please enter a positive integer.")



def display_cart(cart):
    if not cart:
        print("Your cart is empty.")
        return
    
    total_cost = 0
    cart_items = []
    for item in cart:
        product_name, price, quantity = item
        cost = price * quantity
        total_cost += cost
        cart_items.append(f"{product_name} - ${price} x {quantity} = ${cost}")

    for item in cart_items:
        print(item)
    
    print(f"Total cost: ${total_cost}")



def generate_receipt(name, email, cart, total_cost, address):
    pass

def display_sorted_products(products_list, sort_order):
    if sort_order == "asc":
        sorted_list = sorted(products_list, key=lambda x: x[1])
    elif sort_order == "desc":
        sorted_list = sorted(products_list, key=lambda x: x[1], reverse=True)
    else:
        print("invalid。")
        return []

    for index, (product, price) in enumerate(sorted_list):
        print(f"{index + 1}. product: {product}, price: ${price}")

    return sorted_list



def main():
    cart = []
    print("welcome")
    #name
    while True:
        name = input("enter your name, contain only alphabets:")
        if validate_name(name):
            break
        else:
            print("somethings wrong, plz retry")
            continue
    #email
    while True:
        email = input("enter your email:")
        if validate_email(email):
            break
        else :
            print("something wrong, retry")
            continue
    display_categories()
    print("Here are 4 options\n1.Select a product to buy\n2.Sort the products according to the price\n3.Go back to the category selection\n4.Finish shopping")
    
    #choose
    while True:
        choose_number = int(input("enter your choice"))
        if choose_number > 0 and choose_number < 5 :
            while True :
                match choose_number:
                    case  1 :
                        product_number = input("enter the product number:")
                        product_list = display_categories()
                        if 0 <= product_number < len(product_list):
                            product = product_list[product_number][1]
                        quantity = input("enter the product quantity:")
                        add_to_cart(cart, product, quantity)

                    case 2 :
                        pass
                    case 3 :
                        pass
                    case 4 :
                        break
            break
        else:
            print("invalid number, retry")
            continue
""" The following block makes sure that the main() function is called when the program is run. 
It also checks that this is the module that's being run directly, and not being used as a module in some other program. 
In that case, only the part that's needed will be executed and not the entire program """
if __name__ == "__main__":
    main()
