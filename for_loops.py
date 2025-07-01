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
    # print("something")
    # print(yoruba_names)

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

# story = "Once upon a time"
# Print every 2nd character from the string story i.e
# O
# c
# 
# ...

# for index in range(0, len(story), 2):
#     print(story[index])


# for index in range(0, len(story)):
#     if index % 2 == 0:
#         print(story[index])

# Assignment
# Write a program that takes an integer input from the user and uses a loop to calculate 
# the sum of its digits. Print the sum. Example:
# Input: 1234
# Output: 10 (1+2+3+4)


# num = 1
# total = 0
# result = []
# n = int(input("Input a number: "))
# while num <= n:
#     total += num
#     result.append(str(num))
# num += 1

# print(f"{' + '.join(result)} = {total}")
# 1+2+3+4+5=15



# 2. Collect a string from the user and use loops to count the number of vowels and consonants in the string. Print the counts.
#  Example:
# Input: "hello world"
# Output: Vowels: 3, Consonants: 7

# text = input("Enter a string: ").strip().lower()
# vowel_count = 0
# consonant_count = 0
# vowels = "aeiou"
# for char in text:
#     if char.isalpha(): 
#         if char in vowels:
#             vowel_count += 1
#         else:
#             consonant_count += 1
# print("Vowels:", vowel_count)
# print("Consonants:", consonant_count)

# 3. Write a program that takes an integer input from the user and prints the multiplication table for that number up to 12. Example:
# Input: 5
# Output:
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# ...
# 5 x 12 = 60

# number = int(input("Enter an integer: "))

# for i in range(1, 13):
#     result = number * i
#     print(f"{number} x {i} = {result}")

# 4.Collect a string from the user and use a loop to reverse the string. Print the reversed string. 
# Do not reverse the string using [::-1] or reversed().
# Example:
# Input: "python"
# Output: "nohtyp"

# text = input("Enter a string: ").strip().lower()
# reversed_text = ""
# for char in range(len(text) -1, -1, -1):
#     reversed_text += text[char]
# print(reversed_text)


# 5. Write a program that takes a list of numbers (entered as comma-separated values) from the user and removes any duplicate values.
# Print the new list. Do not use the set() constructor. Use a loop. Example:
# Input: "1, 2, 3, 2, 4, 3"
# Output: [1, 2, 3, 4]

# numbers = input("Enter a list of numbers: ").split()
# duplicate = []
# for num in numbers:
#     if num not in duplicate:
#         duplicate.append(num)
# print(f"List without duplicate: {duplicate}")


# 6. Write a program that takes an integer input n from the user and prints the first 
	# n numbers in the Fibonacci sequence. Example:
	# Input: 10
	# Output: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

# number = int(input("Enter an integer: "))
# a = 0
# b = 1
# for i in range(number):
#     nextnumber = a + b
#     a = b
#     b = nextnumber
#     print(a, end = "," if i < number-1 else "\n")
# print(i)



# 7. Collect a list of numbers from the user (entered as comma-separated values) and use a 
	# loop to find and print the largest number in the list. Don’t use the built-in max 
    # function or anything similar.
	# Input: "10, 20, 5, 15"
	# Output: 20

# numbers = input("Enter a list of numbers: ").split(",")
# number_string = numbers
# numbers = [int(num) for num in number_string]
# largest_num = numbers[0]  
# for num in numbers:
#     if num > largest_num:
#         largest_num = num
# print(f"Largest number:{largest_num}")

    
# 8. Write a program that takes an integer n from the user and calculates the sum of all 
	# even numbers from 1 to n. Print the sum.
	# Input: 10
	# Output: 30 (2 + 4 + 6 + 8 + 10)

# number = int(input("Enter an integer:"))
# total = 0
# even_numbers = []
# for num in range(number):
#     if num % 2 == 0:
#         total += num
#         even_numbers.append(str(num))
# print(f"{"+".join(even_numbers)}, Total: {total}")



# 9. Collect a string from the user and use a loop to count the frequency of each character 
	# in the string. Print each character along with its frequency. Example:
	# Input: "hello"
	# Output:
# h: 1
# e: 1
# l: 2
# o: 1

# text = input("Enter a string: ").strip().lower()
# char_count = {}
# for char in text:
#     if char in char_count:
#         char_count[char] += 1
#     else:
#         char_count[char] = 1
# for char in char_count:
#     print(f"{char}: {char_count[char]}")

# 10. Write a program that takes an integer n from the user and calculates the sum of 
	# squares of all numbers from 1 to n. Print the sum. Example:
	# Input: 3
	# Output: 14 (1^2 + 2^2 + 3^2)

# number = int(input("Enter an integer: "))
# total = 0
# result = []
# for num in range(1, number + 1):
#     total += num * num 
#     result.append(str(num))
# print(f"The sum of int: {number} is {total}.  output: {"^".join(result)}")


# 11. 	Collect a phrase from the user and use a loop to generate an acronym by taking the first
	# letter of each word. Print the acronym. Example:
	# Input: "Portable Network Graphics"
	# Output: "PNG"

# phrase = input("Enter a phrase: ").split()
# output = ""
# for i in phrase:
#     output += i[0]
# print(output)

# 12.  Collect a string from the user and use a loop to count the number of words in the string. 
	# Print the count. Example:
	# Input: "Hello world from Python"
	# Output: 4

# text = input("Enter a phrase: ").lower().split()
# count = 0
# for char in text:
#     count += 1
# print(count)

# 13. Collect a string from the user and only print put the words that start with the letter ‘S’. Example:
	# Input: “Print only the words that start with s in this sentence”
	# Output: 
    # start
	# s
	# Sentence


# sentence = input("Enter a sentence: ").lower().split(" ")
# output = sentence
# for char in sentence:
#    if char.startswith('s'):
#      print(char)

# 14. Print all the even numbers from 1 to 20 using the range function and a loop.

# even_numbers = range(1, 21)
# for num in even_numbers:
#     if num % 2 == 0:
#         print(num)
    
# 15.  Use a list comprehension to create a list of numbers between 1 and 50 that are divisible
	# by 3.

# numbers = range(1, 50)
# for num in numbers:
#     if num % 3 == 0:
#         print(num)


# 16. Go through the string below and if the length of a word is even, print that word.
	# st = ‘Print every word in this sentence that has an even number of letters’
	# Output: 
	# word
	# in
	# this
	# sentence
	# that
	# an
	# even
	# number
	# of

# st = "Print every word in this sentence that has an even number of letters"
# st = st.split()
# for char in st:
#     if len(char) % 2 == 0:
#         print(char)


# 17.  	Write a program that prints the integers from 1 to 100. But for multiples of three, print 
	# “Fizz” instead of the number, and for multiples of five, print “Buzz”. For numbers which 
	# are multiples of both three and five, print “FizzBuzz”.

# numbers = range(1, 100)
# for num in numbers:
#     if num % 3 == 0 and num % 5 == 0:
#         num == "FizzBuzz"
#         print(f"{num}: FizzBuzz")
#     elif num % 3 == 0:
#         num == "Fizz"
#         print(f"{num}: Fizz")
#     elif num % 5 == 0:
#         num == "Buzz"
#         print(f"{num}: Buzz")
    

# 1. You are given two lists, names and grades. Print them together
# names = ['Ken', 'Mia', 'Rose', 'Henry', 'Suzan']
# grades = ['A', 'E', 'F', 'C', 'B']

# for name, grade in zip(names, grades):
#     print(f"{name} got grade {grade}")



# 2.  Print only the items at even indexes
# items = ['zero', 'one', 'two', 'three']

# for i, item in enumerate(items):
#     print(f"{i} : {item}")

# 3.# 3 Given two lists of numbers of the same length, print the indices and values of where they differ in a list.
# list1 = [5, 8, 6, 7, 12, 4]
# list2 = [5, 3, 6, 9, 12, 0]
# difference = []
# for index, (val1, val2), in enumerate(zip(list1, list2)):
# 			if val1 != val2:
# 		 		difference.append(f"Index {index}: {list1[index]} != {list2[index]}")
# print(difference)




    
			

# Expected output:
# [
#   'Index 1: 8 != 3',
#   'Index 3: 7 != 9',
#   'Index 5: 4 != 0',
# ]

