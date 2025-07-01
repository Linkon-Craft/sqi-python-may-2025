# class Person:
#     def __init__(self, name, height, complexion, is_male, age):
#         self.full_name = name
#         self.height = height
#         self.complexion = complexion
#         self.is_male = is_male
#         self.age = age


#     def introduce_yourself(self):
#         gender_statement = "I am male" if self.is_male else "I am female"
#         return f"My name is {self.full_name}. {gender_statement}. I am {self.height}m tall. I am {self.complexion} in complexion. I am {self.age} years old."


#     def sing(self, song):
#         return f"{self.full_name} sings {song}"


# molayo = Person("Molayo Mercy", 1.54, "dark", False, 27)
# print(molayo)
# print(molayo.full_name)
# print(molayo.is_male)
# print(molayo.introduce_yourself())
# print(molayo.sing("Heartbreak Anniversary"))
# lekan = Person("Lekan Oyewole", 1.62, "light", True, 30)
# print(lekan)
# print(lekan.full_name)
# print(lekan.is_male)
# print(lekan.introduce_yourself())
# print(lekan.sing("Perfect"))


# Create a class called `Book`.
# The class has the following attributes or properties - title, author, no_of_pages, genre, is_published (True or False)
# The class can print_info() which returns all the necessary info about that particular book
# Then create two different books and call their print_info()
# Also print their title and their author.


# class Book:
#     def __init__(self, title, author, no_of_pages, genre, is_published):
#         self.title = title
#         self.author = author
#         self.no_of_pages = no_of_pages
#         self.genre = genre
#         self.is_published = is_published

#     def print_info(self):
#         print(f"Title: {self.title}")
#         print(f"Author: {self.author}")
#         print(f"Number of pages: {self.no_of_pages}")
#         print(f"Genre: {self.genre}")
#         published = "Yes" if self.is_published else "No"
#         print(f"Is published: {published}")

    
# book1 = Book("Title of Book 1", "Author of Book 1", 23, "fiction", True)
# book2 = Book("Title of Book 2", "Author of Book 2", 200, "Mystery", False)
# book3 = Book("Title of Book 3", "Author of Book 3", 567, "History", False)
# book4 = Book("Title of Book 4", "Author of Book 4", 65, "Adventure", True)

# book1.print_info()
# book2.print_info()
# book3.print_info()
# book4.print_info()

# print(book1.title)
# print(book2.title)
# print(book3.title)
# print(book4.title)

# print(book1.author)
# print(book2.author)
# print(book3.author)
# print(book4.author)


# Forms
# Attendance - Full Name, Time In, Time Out, Signature
# Job Application - Full Name, Resume URL, LinkedIn URL, GitHub URL



# from datetime import datetime, time

# class AttendanceRecord:
#     def __init__(self, full_name: str, time_in: datetime, time_out: datetime, signature: str):
#         self.full_name = full_name
#         self.time_in = time_in
#         self.time_out = time_out
#         self.signature = signature

#     def __str__(self):
#         return f"{self.full_name} | {self.time_in} | {self.time_out} | {self.signature}"


# class AttendancePage:
#     def __init__(self, records: list[AttendanceRecord], page_no: int):
#         self.records = records
#         self.page_number = page_no

#     def __str__(self):
#         header = f"Page {self.page_number}\nFull Name | Time In | Time Out | Signature\n"
#         str_records = [str(record) for record in self.records]
#         return header + "\n".join(str_records)

# class AttendanceBook:
#     def __init__(self, pages: list[AttendancePage]):
#         self.pages = pages

#     def __str__(self):
#         book_pages = [str(page) for page in self.pages]
#         book_pages = "\n".join(book_pages)
#         return f"SQI PYTHON MAY 2025 ATTENDANCE\n{book_pages}"
    
#     def find_late_comers(self, start_time: datetime, end_time: datetime):
#         late_comers = []
#         for page in self.pages:
#             for record in page.records:
#                 if start_time.date() <= record.time_in.date() <= end_time.date():
#                     time_in = record.time_in.time()
#                     if time_in > time(8, 30):
#                         late_comers.append(record.full_name)
#         return late_comers



# record1 = AttendanceRecord("Awwal Abdulwahab", datetime(2025, 6, 18, 8, 10), datetime(2025, 6, 18, 10, 35), "awwal")
# record2 = AttendanceRecord("Omolola Muhammed", datetime(2025, 6, 18, 8, 29), datetime(2025, 6, 18, 3, 47), "lola")
# record3 = AttendanceRecord("Molayo Elemese", datetime(2025, 6, 18, 8, 43), datetime(2025, 6, 18, 4, 25), "mercy")
# record4 = AttendanceRecord("Lekan Oyewole", datetime(2025, 6, 18, 8, 20), datetime(2025, 6, 18, 1, 12), "lekan")

# page1 = AttendancePage([record1, record2], 1)
# page2 = AttendancePage([record3, record4], 100)

# sqi_python_may_2025_attendance = AttendanceBook([page1, page2])

# # print(sqi_python_may_2025_attendance)
# print(sqi_python_may_2025_attendance.find_late_comers(datetime(2025, 6, 1), datetime(2025, 6, 30)))


# Create a class called CartItem.
# A CartItem has a name, a price, and a quantity
# Also create a class called Cart
# A cart is a list of CartItems
# A cart can print the total price of CartItems in it

# Ex
# class CartItem:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#     def total_price(self):
#         return self.price * self.quantity
    
# class Cart:
#     def __init__(self, cart_items: list[CartItem]):
#         self.cart_items = cart_items

#     def total(self):
#         total_price_cart = 0
#         for cart_item in self.cart_items:
#             total_price_cart += cart_item.total_price()
#         return total_price_cart
    

# cart_item1 = CartItem("eggs", 250, 4)
# cart_item2 = CartItem("bread", 1200, 6)
# print(cart_item1.total_price()) # -> 1000
# print(cart_item2.total_price()) # -> 7200
# cart = Cart([cart_item1, cart_item2])
# print(cart.total()) # -> 8200


# class CartItem:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity

    
# class Cart:
#     def __init__(self, cart_items: list[CartItem]):
#         self.cart_items = cart_items

#     def total(self):
#         total_price_cart = 0
#         for cart_item in self.cart_items:
#             total_price = cart_item.price * cart_item.quantity
#             total_price_cart += total_price
#         return total_price_cart

# cart_item1 = CartItem("eggs", 250, 4)
# cart_item2 = CartItem("bread", 1200, 6)
# cart = Cart([cart_item1, cart_item2])
# print(cart.total()) # -> 8200

# PI = 22/7

# class Circle:

#     PI = 3.14

#     def __init__(self, radius=12):
#         self.radius = radius

#     @property
#     def diameter(self):
#         return self.radius * 2
    
#     def show_pi(self):
#         # return self.PI
#         return Circle.PI
    
# circle = Circle(3)
# circle2 = Circle(5)
# circle3 = Circle()
# print(circle.diameter())
# print(circle.diameter)
# print(circle.PI)
# print(circle2.PI)
# print(PI)
# print(circle3.show_pi())
# print(circle3.radius)
# print(circle3.diameter)
# print(circle.show_pi())
# print(circle2.show_pi())




# Assignment
# Fill in the Line class methods to accept coordinates as a pair of tuples and 
# return the slope and distance of the line. Look up the formulas for finding the distance and slope of a line.
# 
# 
# class Line:
#     def __init__(self, coor1, coor2): 
#         self.x1, self.y1 = coor1
#         self.x2, self.y2 = coor2
    
#     def distance(self):
#         return ((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)

#     def slope(self):
#         return (self.y2 - self.y1) / (self.x2 - self.x1)


# coordinatel = (3,2)
# coordinate2 = (8,10)

# line_1 = Line(coordinatel, coordinate2)

# print(line_1.distance())  # 9.433981132056603
# print(line_1.slope())  # 1.6



# Fill in the class

class Cylinder:
    pi = 3.14
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius
    def volume (self):
        volume = round(self.pi * self.radius**2 * self.height, 2)
        return(volume)

    def surface_area(self):
        surface_area = round(2 * self.pi * self.radius * self.height + 2 * self.pi * self.radius ** 2, 1) 
        return(surface_area)
# EXAMPLE EXECUTION

cylinder = Cylinder(2,3)
print(cylinder.volume())  # 56.52
print(cylinder.surface_area())  # 94.2


