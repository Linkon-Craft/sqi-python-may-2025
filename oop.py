# class Book:
#     def __init__(info, title, author, no_of_pages, genre, is_published):
#         info.title = title
#         info.author = author
#         info.no_of_pages = no_of_pages
#         info.genre = genre
#         info.is_published = is_published

#     def print_info(info):
#         published = "Published" if info.is_published else "Not Published"
#         return f"The name of my book {info.title}. published by {info.author}"


# Book1 = Book("The great Pastor", "Benjamen Lawson", "420", "Religion", True)

# Book2 = Book("Angela", "Laura John", "320", "Love", False )

# print(Book1.print_info())
# print(Book2.print_info())
# print(Book1.title)
# print(Book2.title)
# print(Book1.author)
# print(Book2.author)


class CartItem:
    def __init__(self, name: str, price: int, quantity: int):
        self.name = name
        self.price = price
        self.quatity = quantity

    def total_price(self, ):
        total_price = self.price * self.quatity

       

class Cart:
    def __init__(self, name, total_price, quantity):
        self.name = name
        self.total_price = total_price
        self.quatity = quantity





cart_item1 = CartItem("Milk", 700, 2)
cart_item2 = CartItem("Indomie", 350, 4)
cart_item1.total_price()
cart = Cart([cart_item1, cart_item2])





     # if self.fuel > 100:
        #     print(f"Lauching{self.name}")
        #     used_fuel = 50
        #     new_self_fuel = self.fuel - used_fuel
        #     return f"Fuel after launch : {self.fuel} - {used_fuel} = {new_self_fuel}"