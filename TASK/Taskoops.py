# create class product
# prodbname
# prodprice
# prod description
# display all proddetails(using get prod details)
# add to cart
# add product(prod name,price,description)
# id auto generated

# import uuid

# class Product:
   
#     product_list = []

#     def __init__(self, name, price, description):
#         self.id = str(uuid.uuid4())  
#         self.name = name
#         self.price = price
#         self.description = description

    
#         Product.product_list.append(self)

#     def get_prod_details(self):
#         """Return the product details."""
#         return {
#             'ID': self.id,
#             'Name': self.name,
#             'Price': self.price,
#             'Description': self.description
#         }

#     @classmethod
#     def display_all_prod_details(cls):
#         """Display details of all products."""
#         if not cls.product_list:
#             print("No products available.")
#             return
        
#         for product in cls.product_list:
#             details = product.get_prod_details()
#             print(f"ID: {details['ID']}")
#             print(f"Name: {details['Name']}")
#             print(f"Price: {details['Price']}")
#             print(f"Description: {details['Description']}")
#             print("-" * 40)

# class Cart:
#     def __init__(self):
#         self.items = []

#     def add_to_cart(self, product):
#         """Add a product to the cart."""
#         if not isinstance(product, Product):
#             print("Error: The item added is not a product.")
#             return
#         self.items.append(product)
#         print(f"Added {product.name} to the cart.")

#     def display_cart(self):
#         """Display all items in the cart."""
#         if not self.items:
#             print("Cart is empty.")
#             return
        
#         for product in self.items:
#             details = product.get_prod_details()
#             print(f"ID: {details['ID']}")
#             print(f"Name: {details['Name']}")
#             print(f"Price: {details['Price']}")
#             print(f"Description: {details['Description']}")
#             print("-" * 40)

# def get_user_input():
#     """Get input from the user for adding products and interacting with the cart."""
#     cart = Cart()

#     while True:
#         print("1. Add Product")
#         print("2. Display All Products")
#         print("3. Add Product to Cart")
#         print("4. Display Cart")
#         print("5. Exit")
#         choice = input("Enter your choice: ")

#         if choice == '1':
#             name = input("Enter product name: ")
#             price = float(input("Enter product price: "))
#             description = input("Enter product description: ")
#             Product(name, price, description)
#             print("Product added successfully.")

#         elif choice == '2':
#             Product.display_all_prod_details()

#         elif choice == '3':
#             prod_id = input("Enter the ID of the product to add to cart: ")
#             product = next((p for p in Product.product_list if p.id == prod_id), None)
#             if product:
#                 cart.add_to_cart(product)
#             else:
#                 print("Product not found.")

#         elif choice == '4':
#             cart.display_cart()

#         elif choice == '5':
#             print("Exiting...")
#             break

#         else:
#             print("Invalid choice. Please enter a number between 1 and 5.")

# if __name__ == "__main__":
#     get_user_input()
#  
class FoodItem:
    food_id = 1
    
    def __init__(self, name, price, description):
        self.food_id = FoodItem.food_id
        FoodItem.food_id += 1
        self.name = name
        self.price = price
        self.description = description
    
    def food_details(self):
        return {
            'Food ID': self.food_id,
            'Name': self.name,
            'Price': self.price,
            'Description': self.description
        }

class Cart:
    def __init__(self):
        self.food_items = []
    
    def add_food_item(self, food_item):
        self.food_items.append(food_item)
        print(f"Food item added to the cart.")
    
    def display_cart(self):
        for food_item in self.food_items:
            details = food_item.food_details()
            print(f"ID: {details['Food ID']}, Name: {details['Name']}, Price: {details['Price']}, Description: {details['Description']}")

def main():
    cart = Cart()
    
    while True:
        print("\nOptions:")
        print("1. Add Food Item")
        print("2. View Cart")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            name = input("Enter food name: ")
            price = float(input("Enter food price: "))
            description = input("Enter food description: ")
            
            food_item = FoodItem(name, price, description)
            cart.add_food_item(food_item)
        
        elif choice == '2':
            cart.display_cart()
        
        elif choice == '3':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
