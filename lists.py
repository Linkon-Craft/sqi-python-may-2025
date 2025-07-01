# Collections:
# Lists
# Tuples
# Sets
# Dictionaries


jollof_rice_shopping_list = ["rice", "tomato paste", "groundnut oil", "spices", "chicken", "margarine", "green beans", "rice"]

# print(jollof_rice_shopping_list)

# print(jollof_rice_shopping_list[3])

# print(jollof_rice_shopping_list[3][2])
# print("spices"[2])


# Lists are ordered
# Lists are indexed
# Lists are mutable
# lists allow duplicate values

# print("before: ", jollof_rice_shopping_list)
# jollof_rice_shopping_list[4] = "meat"
# jollof_rice_shopping_list.append("onions")

# jollof_rice_shopping_list.remove("green beans")



# jollof_rice_shopping_list.remove("green")

# print("after:  ", jollof_rice_shopping_list)

# ingredient = "chicken"
# ingredient[0] = "h"
# print(ingredient)


# jollof_rice_shopping_list = ["rice", "tomato paste", "groundnut oil", "spices", "chicken", "margarine", "green beans", "rice"]
# jollof_rice_shopping_list.remove("green beans")
# print(jollof_rice_shopping_list)


# jollof_rice_shopping_list = ["rice", "tomato paste", "groundnut oil", "spices", "chicken", "margarine", "green beans", "rice"]


# print("before: ", jollof_rice_shopping_list)
# jollof_rice_shopping_list.remove("chicken")  # list methods work in place
# jollof_rice_shopping_list.append("onions")
# print("Rice" in jollof_rice_shopping_list)

# jollof_rice_shopping_list.insert(4, "crayfish")
# jollof_rice_shopping_list.insert(2, "curry")

# print("after:  ", jollof_rice_shopping_list)


# day_of_the_week = "Tuesday"
# day_of_the_week_upper = day_of_the_week.upper()
# print(day_of_the_week)
# print(day_of_the_week_upper)


# Lists are ordered
# Lists are indexed
# Lists are mutable
# lists allow duplicate values



# Create a list called `sports` that contains "Basketball", "Volleyball", "Tennis", "Golf"
# Print how many items are in the list
# Add "Baseball" to the end of the list
# Remove "Volleyball" from the list
# Print the "ball" in "Basketball"
# Add "Hockey" inbetween "Tennis" and "Golf"
# Check if "Rugby" is in the list
# Print the 2nd item in the list



# sports = ["Basketball", "Volleyball", "Tennis", "Golf"]
# print(len(sports))
# sports.append("Baseball")
# # print("Sade".upper())
# sports.remove("Volleyball")
# print(sports[0][6:])
# sports.insert(2, "Hockey")
# print(sports)
# print("Rugby" in sports)
# print(sports[1])


# sports = ["Basketball", "Volleyball", "Tennis", "Golf"]
# # print(sports[0:3])
# # sports[0:3] = ["Rugby"]
# sports[0] = "Rugby"
# # sports[0] = ["Rugby"]
# print(sports)


# numbers = [98, 23, 67.8, 12, 7.6]

# # numbers[1:4] = [2]
# numbers[1:2] = [20]
# # numbers[1:2] = [2]

# # numbers[3] = 10

# print(numbers)


# numbers = [98, 23, 67.8, 12, 7.6]
# print(numbers[-1])
# print(type(numbers))


# my_list = ["Hey", 9, True, 12, 2.5, None]
# print(my_list)

# my_dict = {"tomato": 7800, "onions": 2300}
# print(my_dict)

# my_tuple = ("John", "Mary", "Hilda", "Timmy")
# # my_list = list(my_tuple)
# # print(my_list)
# print(my_tuple)


# data = ("John", "Mary", "Hilda", "Timmy")
# print(type(data))
# data = list(data)
# print(type(data))
# print(data)

# brand = "Gucci"
# print(list(brand))

# sentence = "I love Teslas"
# print(sentence.split(" "))
# # sentence = list(sentence)
# print(sentence)

# depts = ["Data Science", "Data Analysis", "Software Engineering"]

# other_depts = ["UI/UX", "Graphics Design", "AI"]
# other_depts = ("UI/UX", "Graphics Design", "AI")

# depts.extend(other_depts)
# other_depts.extend(depts)
# print(depts)  # ["Data Science", "Data Analysis", "Software Engineering"]
# print(other_depts)  # ["UI/UX", "Graphics Design", "AI", "Data Science", "Data Analysis", "Software Engineering"]



# depts = ["Data Science", "Data Analysis", "Software Engineering"]
# other_depts = ["UI/UX", "Graphics Design", "AI"]
# # all_depts = depts + other_depts
# # print(all_depts)
# print(depts + other_depts)



# sqi_depts = ["UI/UX", "Graphics Design", "AI"]
# sqi_depts.remove("AI")
# del sqi_depts[2]
# del sqi_depts
# print(sqi_depts)  # NameError

# sqi_depts.pop(2)
# print(sqi_depts)


# sqi_depts = ["UI/UX", "AI", "Graphics Design", "AI"]
# print("before: ", sqi_depts)
# sqi_depts.remove("AI")
# # del sqi_depts[2]
# # print(sqi_depts)
# popped_item = sqi_depts.pop(3)
# popped_item = sqi_depts.pop()
# popped_item = sqi_depts.pop(0)
# print("after:  ", sqi_depts)
# print(popped_item)


# sqi_depts = ["UI/UX", "AI", "Graphics Design", "AI"]
# del sqi_depts
# print(sqi_depts)

# num = 5
# del num
# print(num)


# depts = ["Data Science", "Data Analysis", "Software Engineering"]
# depts.clear()
# print(depts)

# depts = ["Data Science", "Data Analysis", "Software Engineering"]
# depts = []
# print(depts)


# depts = ["Data Science", "Data Analysis", "Software Engineering"]
# # depts.sort()
# depts.sort(reverse=False)
# # depts.sort(reverse=True)
# print(depts)

# fruits = ["Apple", "Grape", "orange", "banana"]
# # ["Apple", "banana", "Grape", "orange"]
# # fruits.sort()  # case sensitive sort
# fruits.sort(key=str.lower)  # case-insensitve sort
# print(fruits)


# fruits = ["Apple", "Grape", 12, "orange", "banana"]
# fruits.sort()
# print(fruits)

# fruits = ["Apple", "Grape", 12, "orange", "banana"]
# ["banana", "orange", 12, "Grape", "Apple"]
# print("before: ", fruits)
# fruits.reverse()
# print("after:  ", fruits)


# fruits = ["Apple", "Grape", 12, "orange", "banana"]
# fruits = fruits[::-1]
# print(fruits)

# colors = ["red", "violet", "rebecca purple", "cyan", "white"]
# colors_copy = colors  # reference
# print("before colors     ", colors)
# print("before colors_copy", colors_copy)


# colors.append("black")
# print("after colors      ", colors)
# print("after colors_copy ", colors_copy)


# colors = ["red", "violet", "rebecca purple", "cyan", "white"]
# colors_copy = colors.copy()  # true copy
# print("before colors     ", colors)
# print("before colors_copy", colors_copy)


# colors.append("black")
# print("after colors      ", colors)
# print("after colors_copy ", colors_copy)

# import copy
# nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# nums_copy = copy.copy(nums)  # copies only outer elements
# nums_copy = copy.deepcopy(nums)  # copy nested elements

# nums = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print(nums[1][1])
# print(nums[0][2])
# print(nums[-1][-3])
# print(nums[1][0:2])


# nested_list = [
#     ["Alice", "Bob"],
#     [10, 20, 30],
#     [True, False]
# ]
# print(nested_list[1][1] + nested_list[1][2])
# print(nested_list[0][0][2:])
# Alibob
# print(nested_list[0][0][0:3] + nested_list[0][1][0:])
# nested_list[2][1] = 20
# print(nested_list)

# nested_list[2][0] = int(nested_list[2][0])
# print(nested_list)



# Assignment
# 1.Create a list called fruits with items "apple", "banana", and "orange". Print the first item.
fruits = ["apple", "banana", "orange"]
print(fruits[0])

# 2. Create a list called colors with items "red", "green", "blue". Print the last item using negative indexing.
colors = ["red", "green", "blue"]
print(colors[-1])

# 3. Create a list called numbers with items from 1 to 10. Print items from index 3 to index 7.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[3:8])

# 4. Create a list called alphabets with items "a", "b", "c", ..., "z". Print a slice from index -3 to the end.
alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
print(alphabets[-3:])

# 5. Create a list called ages with items 20, 30, 40. Change the value of the second item to 35.
ages = [20, 30, 40]
ages[1] = 35
print(ages)

# 6. Create a list called grades with items "A", "B", "C", "D". Change the values of items from index 1 to index 3 to "X".
grades = ["A", "B", "C", "D"]
grades[1:3] = "X"
print(grades)

# 7 Create a list called cities with items "New York", "London", "Paris". Insert "Tokyo" at the beginning of the list.
cities = ["New York", "London", "Paris"]
cities.insert(0, "Tokyo")
print(cities)

# 8. Create a list called fruits with items "apple", "banana", "cherry". Print the number of items in the list.
fruit = ["apple", "banana", "cherry"]
print(len(fruit))

# 9. Create a list called prices with items 10.5, 20.0, 15.75. Print the data type of the list.
prices = [10.5, 20.0, 15.75]
print(type(prices))

# 10. Create a list called mixed with items 10, "apple", True. Print the list.
mixed = [10, "apple", True]
print(mixed)

# 11. Create a tuple called tuple_data with items "a", "b", "c". Convert the tuple into a list.
tuple_data = "a", "b", "c",
print(list(tuple_data))

# 12. Create a list called books with items "Python", "Java". Append "JavaScript" to the end of the list.
books = ["Python", "Java"]
books.append("JavaScript")
print(books)

# 13. Create a list called names with items "Alice", "Bob", "Eve". Insert "Charlie" at index 1.
names = ["Alice", "Bob", "Eve"]
names.insert(1, "Charlie")
print(names)

# 14. Create two lists called list1 and list2 with items 1, 2, 3 and 4, 5, 6 respectively. Extend list1 with list2.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)

# 15. Create a list called students with items "Alice", "Bob". Add items from a tuple ("Charlie", "David") to students.
students = ["Alice", "Bob"]
tuples = ("Charlie", "David")
students.append(tuples[1])
print(students)

# 16. Create a list called colors with items "red", "green", "blue". Remove "green" from the list.
color = ["red", "green", "blue"]
color.remove("green")
print(color)

# 17. Create a list called numbers with items 10, 20, 30, 40. Use the del keyword to remove the item at index 2.
number = [10, 20, 30, 40]
del number[2]
print(number)

# 18. Create a list called fruits with items "apple", "banana", "cherry". Clear the list.
fruts = ["apple", "banana", "cherry"]
fruts.clear()
print(fruts)

# 19. Create a list called names with items "Zoe", "Alice", "Bob". Sort the list alphabetically.
name = ["Zoe", "Alice", "Bob"]
name.sort()
print(name)

# 20. Create a list called ages with items 25, 35, 20. Sort the list in descending order.
age = [25, 35, 20]
age.sort(reverse= -1)
print(age)

# 21. Sorting lists is CASE-SENSITIVE by default. Create a list called words with items 
# "Apple", "banana", "Orange". Sort the list in CASE-INSENSITIVE alphabetical order.
words = ["Apple", "banana", "Orange"]
words.sort(key=str.lower) 
print(words)

# 22. Create a list called numbers with items 1, 2, 3, 4. Print the list in reverse order.
numberss = [1, 2, 3, 4]
numberss.reverse()
print(numberss)

# 23. Create a list called letters with items "a", "b", "c", "d". Print the list in reverse order using slicing
letters = ["a", "b", "c", "d"]
letters = letters[::-1]
print(letters)

# 24. 	Create a list called original with items "one", "two", "three". Create a copy of the list.
import copy
original = ["one", "two", "three"]
original_copy = copy.copy(original)
print(original)
print(original_copy)

# 25. Create two lists called list1 with items "a", "b" and list2 with items "c", "d". Join list1 and list2 together.
lit1 = ["a", "b"]
lit2 =["c", "d"]
lit1.extend(lit2)
print(lit1)

# 26. Access and print the second subject of the first person in the list.
data = [
["Alice", 25, ["Math", "Physics"]],
["Bob", 30, ["Chemistry", "Biology"]],
["Charlie", 35, ["History", "Geography"]] 
]
print(data[0][2][0])

# 27. Access and print the first value in the list of numbers associated with "San Francisco".
records = [
["New York", [10, 20, 30]],
["San Francisco", [40, 50, 60]],
["Austin", [70, 80, 90]]
]
print(records[1][1][0])

# 28. Get the first e in Ayo’s gender and Get Ben’s age.
group = [
["Ayo", ["Female", 12]],
["Ben", ["Male", 9]]
]
print(group[0][1][0][5])
print(group[1][1][1])

# 29. Get the l in Nina’s gender and Get Tobi’s age
record = [
["Tobi", ["Male", [6]]],
["Nina", ["Female", [7]]]
]
print(record[1][1][0][4])
print(record[1][1][1])

# 30. Get the two oo’s in X1’s 2nd mobility status (loose) together (slicing) and Get the battery percentage of R2
robot_grid = [
["R2", ["battery", [98]]],
["R5", ["status", "active"]],
["X1", [["joint", "loose"], "error"]]
]
print(robot_grid[2][1][0][1][1:3])
print(robot_grid[0][1][1])

# 31. Get the Five in the jazz song title and Get the duration of the Jazz song
playlist = [
["Jazz", ["Take Five", 5.24]],
["Pop", ["Blinding Lights", 3.20]],
["Rock", ["Bohemian Rhapsody", 5.55]]
]
print(playlist[0][1][0][5:9])
print(playlist[0][1][1])

# 32. Get the letter v in Tiger’s category and Get the first letter of the Frog’s type
animals = [
["Elephant", ["Herbivore"]],
["Tiger", ["Carnivore"]],
["Frog", ["Amphibian"]]
]
print(animals[1][1][0][5])
print(animals[2][1][0][0])



# Assignment 2
