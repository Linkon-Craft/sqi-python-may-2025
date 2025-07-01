
# 1.students_scores = (("Alice", 85), ("Bob", 92), ("Charlie", 78))
# Unpack the tuple and print the name of the student who scored above 90.

# students_scores = (("Alice", 85), ("Bob", 92), ("Charlie", 78))
# name_score1, name_score2, name_score3 = students_scores
# print(students_scores[1][0])



# books = (("Python 101", 200), ("AI Basics", 150), ("Data Science", 300))
# # Loop through the tuple, unpack each book, and print only the book titles
# # that have more than 180 pages.
# Swapping Values with Tuple Unpacking

# books = (("Python 101", 200), ("AI Basics", 150), ("Data Science", 300))
# (book1, page1), (book2, page2), (book3, page3) = books
# print(book1, book2, book3)

# python
# Copy
# Edit
# coords = ((10, 20), (30, 40))
# Swap the two coordinate pairs and print the result.

# coords = ((10, 20), (30, 40))
# ((30, 40), (10, 20)) = coords
# print(coords)


# 🔵 Advanced Level
# Complex Tuple Structure Unpacking

# python
# Copy
# Edit
# data = (("user1", (25, "Engineer")), ("user2", (30, "Designer")), ("user3", (22, "Analyst")))
# # Unpack the data and print the profession of the youngest user.
# Aggregate Using Tuple Unpacking

# data = (("user1", (25, "Engineer")), ("user2", (30, "Designer")), ("user3", (22, "Analyst")))
# user1, user2, user3 = data
# print(data[2][1][1])


# python
# Copy
# Edit
# expenses = (("January", (1200, 300)), ("February", (1100, 400)), ("March", (1300, 250)))
# # Unpack and calculate the total amount spent in each month.
# Conditional Logic with Tuple Elements

# expenses = (("January", (1200, 300)), ("February", (1100, 400)), ("March", (1300, 250)))
# january, february, march = expenses
# print(expenses[0][1][0] + expenses[0][1][1])
# print(expenses[1][1][0] + expenses[1][1][1])
# print(expenses[2][1][0] + expenses[2][1][1])


# python
# Copy
# Edit
# temperatures = (("Mon", 21), ("Tue", 19), ("Wed", 24), ("Thu", 22), ("Fri", 20))
# # Unpack the data and print the name of the day(s) with temperatures above 21.

# temperatures = (("Mon", 21), ("Tue", 19), ("Wed", 24), ("Thu", 22), ("Fri", 20))
# mon, tue, wed, thu, fri = temperatures
# print(temperatures[2], temperatures[3])


# Problem: Write a program that asks the user to input their name and age, separated by a comma (e.g., "Alice, 25"). 
# Store the input in a tuple, unpack it, and print a greeting. If the age is less than 18, print a message saying they are too 
# young to vote; otherwise, say they can vote.

