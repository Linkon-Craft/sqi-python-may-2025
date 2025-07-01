# event = "birthday"

# i = 0

# while i < len(event):
#     char = event[i]
#     print(char)
#     i += 1

# event = "birthday"
# for char in event:
#     print(char)

# yoruba_names = ["Abike", "Adebisi", "Folorunsho", "Kilanko", "Araire", "Desire", "Alubankudi"]

# for yoruba_name in yoruba_names:
#  print("something")
# # print(yoruba_names)

# for name in yoruba_names:
#     print(name)


# professions = ('teaching', 'law', 'software engineer', 'medicine', 'accounting', 'automobile engineering')
# for profession in professions:
#     print(profession)

# my_dream_job = {"dreamer": "Ms. Molayo", "dream_job": "Data Analyst", "dream_salary": 1_000_000_000}

# for key in my_dream_job:
#     print(key)

# for item in my_dream_job.items():
#     print(item)

# for key, value in my_dream_job.items():
#     print(f"{key} -> {value}")


# states_and_capitals = {"Anambra": "Awka", "Lagos": "Ikeja", "Oyo": "Ibadan", "Osun": "Osogbo", "Ogun": "Abeokuta"}
# for state, capital in states_and_capitals.items():
#     print(f"The capital of {state} is {capital}")

# actions = ["run", "jump", "stop", "walk"]

# for action in actions:
#     if action == "stop":
#         break
#     print(action)

# actions = ["run", "jump", "stop", "walk"]
# for action in actions:
#     if action == "jump":
#         continue
#     print(action)

# print(list(range(35)))
# print(list(range(1, 35)))
# print(list(range(1, 35, 2)))
# print(list(range(2, 35, 2)))
# print(list(range(35, 2, -1)))

# for num in range(35):

#     print(num)

# print all the even numbers between 12 and 20, do not use any if statements


# print(list(range(12, 21, 2)))

# story = "Once upon a time"
# Print every 2nd character from the string story i.e
# O
# c
# story = "Once upon a time"
# for char in len(story):
#     print(story[::2])
...

# for index in range(0, len(story), 2):
#     print(story[index])


# for index in range(0, len(story)):
#     if index % 2 == 0:
#         print(story[index])


# =============================================Assignmnet correction=============================================
# 5, 6, 9
# 5. Write a program that takes a list of numbers (entered as comma-separated values) from the user and removes any duplicate values. Print the new list. Do not use the set() constructor. Use a loop. Example:
# Input: "1, 2, 3, 2, 4, 3"
# Output: [1, 2, 3, 4]

# numbers = input("Enter comma-separated numbers: ").split(",")

# unique_numbers = []

# for number in numbers:
#     number = int(number)
#     if number in unique_numbers:
#         continue
#     unique_numbers.append(number)


# print(unique_numbers)
# numbers = input("Enter comma-separated numbers: ").split(",")

# unique_numbers = []

# for number in numbers:
#     number = int(number)
#     if number not in unique_numbers:
#         unique_numbers.append(number)

# print(unique_numbers)

# 6. Write a program that takes an integer input n from the user and prints the first
# n numbers in the Fibonacci sequence. Example:
# Input: 10
# Output: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
# DSA -> Data Structures and Algorithms
# n = int(input("Enter the number of numbers you want in the fibonacci sequence: "))

# fibonacci = [0, 1]

# i = 0
# while i < n - 2:
#     first_num = fibonacci[i]
#     second_num = fibonacci[i+1]
#     next_num = first_num + second_num
#     fibonacci.append(next_num)
#     i += 1

# print(fibonacci)

# fibonacci = [0, 1]

# for i in range(0, n - 2):
#     first_num = fibonacci[i]
#     second_num = fibonacci[i+1]
#     next_num = first_num + second_num
#     fibonacci.append(next_num)

# print(fibonacci)

# 9. Collect a string from the user and use a loop to count the frequency of each character
# in the string. Print each character along with its frequency. Example:
# Input: "hello"
# Output:
# h: 1
# e: 1
# l: 2
# o: 1

# text = input("Enter some text: ").strip().lower()

# occurences = {}

# for char in text:
#     if char in occurences:
#         occurences[char] += 1
#     else:
#         occurences[char] = 1

# print(occurences)


# =============================================Assignmnet correction=============================================


# ENUMERATE
# using while loops
# text = "Tuesday"
# index = 0
# while index < len(text):
#     char = text[index]
#     print(char)
#     index += 1


# text = "Tuesday"
# for index in range(len(text)):
#     char = text[index]
#     print(char)


# colors = ["red", "orange", "purple", "black", "silver", "blue"]
# for index in range(len(colors)):
#     char = colors[index]
#     print(char)

# colors = ["red", "orange", "purple", "black", "silver", "blue"]

# print(list(enumerate(colors)))

# for index, color in enumerate(colors):
#     print(f"Index of {color} is {index}")

# for index, _ in enumerate(colors):
#     print(index)

# sports = ["Basketball", "Volleyball", "Tennis", "Swimming"]

# Output:
# Sports #1 -> Basketball
# Sports #s -> Volleyball
# Sports #1 -> Tennis
# Sports #1 -> Swimming



# for index, sport in enumerate(sports):
#     print(f"Sport #{index + 1} -> {sport}")

# i = 0
# while i <= 10:
#     print(i)
#     i += 1
# else:
#     print("loop has stopped")


# for i in range(11):
#     print(i)
# else:
#     print("loop has stopped")


# sports = ["Basketball", "Volleyball", "Tennis", "Swimming"]

# for i, sport in enumerate(sports):
#     print(f"{i+1}: {sport}")
# for j, char in enumerate(sports):
#     print(f"{j+1}: {char}")


# a) Basketball
# b) Volleyball

# import string
# alphabets = string.ascii_lowercase
# print(alphabets)

# sports = ["Basketball", "Volleyball", "Tennis", "Swimming"] * 2

# print(list(zip(alphabets, sports)))

# for letter, sport in zip(alphabets, sports):
#     print(f"{letter}). {sport}")


# adjectives = ["fierce", "majestic", "playful"]
# animals = ["lion", "eagle", "dolphin"] 

# for adjective in adjectives:
#     for animal in animals:
#         print(f"{adjective} {animal}")

# for num in [1, 2, 3]:
#     print(num)
#     pass
 
# print("something")    #Loops: When a loop is needed but no action is required within the loop body.



# ===================================ASSIGNMENT===================================
# Use only for loops for the problems below:

# 1. You are given two lists, names and grades. Print them together
names = ['Ken', 'Mia', 'Rose', 'Henry', 'Suzan']
grades = ['A', 'E', 'F', 'C', 'B']

# Expected Output:
# Ken got grade A
# Mia got grade E
# Rose got grade F
# Henry got grade C
# Suzan got grade B

# 2. Print only the items at even indexes
items = ['zero', 'one', 'two', 'three']

# Expected Output:
# 0: zero
# 2: two

# 3 Given two lists of numbers of the same length, print the indices and values of where they differ in a list.
list1 = [5, 8, 6, 7, 12, 4]
list2 = [5, 3, 6, 9, 12, 0]

# Expected output:
# [
#   'Index 1: 8 != 3',
#   'Index 3: 7 != 9',
#   'Index 5: 4 != 0',
# ]
# ===================================ASSIGNMENT===================================

