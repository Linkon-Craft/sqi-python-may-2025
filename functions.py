# def my_func():
#     print("This code is running from my_func()")

# my_func()

# def greet(name):
#     print(f"Good morning, {name}")


# my_name = "Winnie"
# greet(my_name)


# def add_2_nums(a, b):
#     print(f"{a} + {b} = {a+b}")

# result = add_2_nums(3, 6)
# print(result)


# def add_2_nums(a, b):
#     return f"{a} + {b} = {a+b}"

# result = add_2_nums(3, 6)
# print(result)

# def add_2_nums(a, b):
#     return f"{a} + {b} = {a+b}"

# result = add_2_nums(3, 6)
# print(result)



# Write a function raise_to_power(base, exponent) that prints the result of base raised to the power of exponent
# my_name = "Winifred"
# my_name_upper = my_name.upper()
# print(my_name_upper)

# def greet(name, time_of_day):
#     return f"Good {time_of_day}, {name}!"

# greeting = greet("Winnie", "morning")
# print(greeting)


# Write a function multiply_nums(num1, num2) that returns the result of multiplying num1 by num2.
# After, print the result of the function

# def multiply_nums(num1, num2):
#     return num1 * num2

# print(multiply_nums(4, 5))


# Write a function that checks if an email address contains "@", ends with ".com" and has at least 8 chard
# If all these are not satsified, the function should return False
# Otherwise, return True 

# def validate_email_address(email: str):
#     has_at_symbol = False
#     ends_with_dot_com = False
#     has_at_least_8_chars = False
#     if "@" in email:
#         has_at_symbol = True
#     if email.endswith(".com"):
#         ends_with_dot_com = True
#     if len(email) >= 8:
#         has_at_least_8_chars = True
#     return has_at_symbol and ends_with_dot_com and has_at_least_8_chars

# print(validate_email_address("winnie@gmail.com"))


# def validate_email_address(email: str):

#     if "@" not in email:
#         return False
    
#     if not email.endswith(".com"):
#         return False
    
#     if len(email) < 8:
#         return False
#     return True

# print(validate_email_address("winniegmail.com"))


# def greet():
#     print("Running from inside greet() func")

# print("Running before greet() call")
# greet()
# print("Running after greet() call")


# Output
# Running before greet() call
# Running form inside greet() func
# Running after greet() call



# Write a function called square_num(num) that returns the square of num
# Print the result

# def square_num(num):
#     # return num * num
#     return num ** 2

# print(square_num(12))


# Write a function that returns True if num is even, otherwise, return False
# Print the result 

# # BEGINNER
# def is_even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False

# print(is_even(13))

# # INTERMEDIATE

# def is_even(num):
#     if num % 2 == 0:
#         return True
#     return False

# print(is_even(13))


# ADVANCED

# def is_even(num):
#     return num % 2 == 0

# print(is_even(13))

# def is_even(num):
#     print(num % 2 == 0)

# print(is_even(13))


# def collect_user_details(first_name, last_name, age, password, confirm_password):

#     return first_name, last_name, age, password, confirm_password

# first_name = input("Enter your first name: ").strip()
# last_name = input(":Enter your last name: ").strip()
# age = int(input("Enter your age: "))
# password = input("Enter your password: ").strip()
# confirm_password = input("Confirm your password: ").strip()
# print(collect_user_details(first_name, last_name, age, password, confirm_password))

# SIGN USERS UP
# 1. Collect the user's details
# 2. Validate the details
# 3. Add them to the fake_db and display a success message

# def collect_user_details():
#     first_name = input("Enter your first name: ").strip()
#     last_name = input("Enter your last name: ").strip()
#     age = int(input("Enter your age: "))
#     password = input("Enter your password: ").strip()
#     confirm_password = input("Confirm your password: ").strip()

#     return first_name, last_name, age, password, confirm_password


# def validate_user_details(first_name, last_name, age, password, confirm_password):
#     if not first_name:
#         print("First name cannot be blank")
#         return False
#     if not last_name:
#         print("Last name cannot be blank")
#         return False
#     if age < 1:
#         print("Age must be positive")
#         return False
#     if not password:
#         print("Password cannot be balnk")
#         return False
#     if not confirm_password:
#         print("Confirm Password cannot be balnk")
#         return False
#     if password != confirm_password:
#         print("Passwords don't match")
#         return False
#     return True
    

# fake_db = []
# def populate_fake_db(first_name, last_name, age, password):
#     fake_db.append({"first_name": first_name, "last_name": last_name, "age": age, "password": password})
    # print(f"{first_name} {last_name} registered successsfully")
    


# while True:
#     first_name, last_name, age, password, confirm_password = collect_user_details()
#     details_are_valid = validate_user_details(first_name, last_name, age, password, confirm_password)
#     if details_are_valid:
#         populate_fake_db(first_name, last_name, age, password)
#     continue_registering = input("Do you want to register another user? (Y/N): ").strip().lower()

#     if continue_registering != "y":
#         # First name: ______, Last name: _______
#         # First name: ______, Last name: _______
#         # First name: ______, Last name: _______
#         # First name: ______, Last name: _______
        # for user in fake_db:
        #     print(f"First name: {user["first_name"]}, Last name: {user["last_name"]}, Age: {user["age"]}")
#         break


# def greet(time_of_day, name="Anonymous"):
#     # return f"Good {time_of_day}, {name}🌻"
#     pass

# print(greet(name="Winnie", time_of_day="morning"))


# *args and **kwargs

# def print_nums(num1, num2, num3):
#     print(num1)
#     print(num2)
#     print(num3)


# print_nums(3, 5, 12)


# def print_nums(*nums):
#     for num in nums:
#         print(num)


# print_nums(3, 5, 12, 34, 768, 1567283, 562, 8992, 1038)


# def add_all_nums(*nums):
#     return sum(nums)


# print(add_all_nums(3, 5, 12, 34, 768, 1567283, 562, 8992, 1038))

# 1578697


# def greet_everyone(*names):
#     for name in names:
#         print(f"Hello, {name} 👋")

# greet_everyone("Winnie", "Awwal", "Lekan", "Molayo", "Omolola")


# Take in an arbitrary number of names and using a list comprehension, turn them all to uppercase
# Your function shoudl return a list of all the names uppercased.

# def uppercase_all_names(*names):
#     return [name.upper() for name in names]

# print(uppercase_all_names("Winnie", "Awwal", "Lekan", "Molayo", "Omolola"))
# ["WINNIE", "AWWAL", "LEKAN", "MOLAYO", "OMOLOLA"]


# Take in an arbitrary number of numbers and using a list comprehension, return a tuple of only the numbers that are greater than 50.

# def filter_out_nums_less_than_50(favorite_num, *nums):
#     print(f"my fave num is {favorite_num}")
#     return tuple([num for num in nums if num > 50])

# print(filter_out_nums_less_than_50(45, 89, 12, 43, 90))
# (89, 90)


# **kwargs
# def states_and_their_capitals(location, **states_and_capitals):
#     print(f"I am currently at {location}")
#     for state, capital in states_and_capitals.items():
#         print(f"The capital of {state} is {capital}")

# # states_and_their_capitals("SQI", oyo="Ibadan", osun="Osogbo", ogun="Abeokuta", ondo="Akure")
# states_and_capitals = {
#     "Oyo": "Ibadan",
#     "Osun": "Osogbo",
#     "ogun": "Abeokuta",
#     "ondo": "Akure",
# }
# states_and_their_capitals("SQI", **states_and_capitals)

# def power(base, exponent):
#     if exponent == 0:  # Base case
#         return 1
#     else:
#         return base * power(base, exponent - 1)  # Recursive call

# power(2, 3)
# 2 * power(2, 2)
# 2 * 2 * power(2, 1)
# 2 * 2 * 2 * power(2, 0)
# 2 * 2 * 2 * 1
# 8

# print(power(2, 1000))


# import random
# print("080" + str(random.randrange(1000000, 9999999)))


# name = "Winnie"

# def my_func():
#     global name
#     name = "Omolola"
#     print(f"Name inside my_func: {name}")

# print(f"Name before func call: {name}")
# my_func()
# print(f"Name after func call: {name}")



# color = "red"

# def some_func(name):
#     """
#     Some func
#     """
#     print(name)
#     print(color)

# some_func("Winnie")

# print(name)


# def add_nums(num1: int, num2: int) -> int:
#     """
#     Add nums num1 and num2 together.
#     Return the result.

#     num1: int
#     num2: int
#     Returns:
#     int
#     """
#     return num1 + num2

# print(add_nums(5, 8))

# help(add_nums)

# Write a function is_alliteration(two_word_string) that takes a two-word string and returns True if both words begin with the same letter.
# is_alliteration(‘Levelheaded llama’) —> True
# is_alliteration(‘Crazy Kangaroo’) –> False


# def is_alliteration(two_word_string: str):
#     word1, word2 = two_word_string.lower().split()
#     first_letter_word_1 = word1[0]
#     second_letter_word_2 = word2[0]
#     return first_letter_word_1 == second_letter_word_2

# print(is_alliteration("Levelheaded Llama"))
# print(is_alliteration("Silicon Valley"))

# def is_alliteration(two_word_string: str):
#     word1, word2 = two_word_string.lower().split()
#     return word1[0] == word2[0]



# =======================================Assignment========================================================================

# 1. Write a function sum_numbers(a, b) that returns the sum of two numbers.
# def sum_numbers(a, b):
#     print(f"{a} + {b} = {a + b}")
# sum_numbers(4, 7)

# 2.Write a function is_even(n) that returns True if n is even and False if n is odd.
# def is_even(n):
#     return n % 2 == 0
# print(is_even(6))

# 3. Write a function is_prime(n) that returns True if n is a prime number and False otherwise.

# def is_prime(n):
#     if n % 2 == 0:
#         return False
#     if n < 2:
#         return False
#     if n == 2:
#         return True
#     if n % 2 == 0 or n % 3 == 0:
#         return False
#     return True
# print(is_prime(31))

# 4. Using the is_prime(n) function from number 3, write a function that asks a user for an input n and returns all the prime 
# numbers up to n.
# def is_prime(n):
#     if n == 2:
#         return True
#     if n == 3:
#         return True
#     if n % 2 == 0:
#         return False
#     if n < 2:
#         return False
#     if n % 2 == 0 or n % 3 == 0:
#         return False
#     return True


# def get_prime():
#     n = int(input("Enter an input n: "))
    
#     prime_numbers = []
#     for num in range(2, n):
#         if is_prime(num):
#             prime_numbers.append((num))
#         if n < 2:
#             print("please enter a number greater than 2")
#             return
#     if prime_numbers:
#         print(f"prime numbers up to {n} are: {prime_numbers}")
#     else:
#         print(f"No prime numbers find up to {n}")
#     return all(prime_numbers)
# get_prime()

    
# Write a function lesser_of_two_evens(a, b) that returns the lesser of two given numbers if both numbers are even,
# but returns the greater if one or both numbers are odd.

# def lesser_of_two_evens(a, b):
#         if a % 2 == 0 and b % 2 == 0:
#             return min(a, b)
#         else:
#             return max(a, b)
# print(lesser_of_two_evens(4, 7))
# print(lesser_of_two_evens(7, 2))
# print(lesser_of_two_evens(8, 4))

    
# 6. Write a function is_alliteration(two_word_string) that takes a two-word string  and returns True if both words begin with the same letter.
# is_alliteration(‘Levelheaded llama’) —> True
# is_alliteration(‘Crazy Kangaroo’) –> False

# def is_alliteration(two_word_string):
#     word1, word2 = two_word_string.lower().split()
#     first_letter = word1[0]
#     second_letter = word2[0]
#     return first_letter == second_letter

# print(is_alliteration("Levelheaded, llama"))
# print(is_alliteration("Crazy, Kangaroo"))

# 7. Write a function old_macdonald(name) that capitalizes the first and fourth letters of a name
# old_macdonald(‘macdonald’) —> MacDonald
# Note: ‘macdonald’.capitalize() returns Macdonald, not MacDonald.

# def old_macdonald(name):
#     if len(name) < 4:
#         print("name must be more than 3 letters")
#     first_letter_name = name[0].upper()
#     midde_part = name[1:3]
#     fourth_letter_name = name[3].upper()
#     rest = name[4:]
#     result = first_letter_name + midde_part + fourth_letter_name + rest 
#     return result
# print(old_macdonald("macdonald"))
        
    
# 8. Write a function spy_game(list_of_ints) that takes in a list of integers and returns True if it contains 007 in order.
# spy_game([1, 2, 4, 0, 0, 7, 5]) —> True
# spy_game([1, 0, 2, 4, 0, 5, 7]) —> True
# spy_game([1, 7, 2, 0, 4, 5, 0]) —> False

# def spy_game(list_of_ints):
#     container = ([0,0,7])
#     code = 0
#     for game in list_of_ints:
#         if game == container[code]:
#             code += 1
#         if code == len(container):
#             return True
#     return False
# print(spy_game([1, 2, 4, 0, 0, 7, 5]))
# print(spy_game([1, 0, 2, 4, 0, 5, 7]))
# print(spy_game([1, 7, 2, 0, 4, 5, 0]))

# 9.Write a function vol(radius) that computes the volume of a sphere given its radius.
# import math
# def vol(radius):
#     volume_sphere = (4/3) * math.pi * (radius ** 3)
#     return volume_sphere
# print(vol(3))

# 10.Write a function range_check(num, low, high) that checks whether a number is in a given range (inclusive of high and low).
# def range_check(num, low, high):
#     if low <= num <= high:
#         print(f"{num} is within range of {low} and {high}")
#         return True
#     print(f"{num} is not within range of {low} and {high}")
#     return False
# range_check(6, 4, 10)
# range_check(12, 5, 9)
# range_check(6, 3, 6)

# 11. Write a function upper_lower(text) that accepts a string and calculates the number of uppercase letters and lowercase letters.

# def upper_lower(text):
#     upper_case = 0
#     lower_case = 0
#     for char in text:
#         if char == char.upper():
#             upper_case += 1
#         if char == char.lower():
#             lower_case += 1
#     print(f"{text} has {upper_case} Uppercase and {lower_case} Lower case")
#     return
# upper_lower("ShANgaInSa")
# upper_lower("LovErEnA")

# 12. Write a function unique_list(list_items) that takes in a list and returns a new list with unique elements of the first list. 
# Do not use the set() constructor.

# def unique_list(list_items):
#     unique_elements = []
#     for num in list_items:
#         if num not in unique_elements:
#             unique_elements.append(num)
#     return unique_elements
# print(unique_list([4,6,3,4,2,9,3,6,5]))

# 13.Write a function multiply(list_items) to multiply all the numbers in a list.
	# Sample List: [1, 2, 3, -4]
	# Expected output: -24

# def multiply(list_items):
#     output = 1
#     for num in list_items:
#         output *= num
#     return output
# print(multiply([1, 2, 3, -4]))

# 14.Write a function is_pangram(text) to check whether a string is a pangram or not. 
	# Note: A pangram is a word or sentence that contains every letter of the alphabet at  
	# least once. For example: “The quick brown fox jumps over the lazy dog”.
	# Hint: Import and use the string module.
# import string
# def is_pangram(text):
#     text = text.lower()
#     all_alphabet = set(string.ascii_lowercase)
#     letter_in_text = set()
#     for char in text:
#         if char.isalpha():
#             letter_in_text.add(char)
#     return letter_in_text >= all_alphabet
# print(is_pangram("The quick brown fox jumps over the lazy dog"))
# print(is_pangram("Hello World"))

# 15. Write a function are_anagrams(s1, s2) that checks if two strings are anagrams of each
	# other. a word, phrase, or name formed by rearranging the letters of another, such as
	# spar, formed from rasp.

# def are_anagrams(s1, s2):
#     return sorted(s1.lower().replace(" ", "")) == sorted(s2.replace(" ", "").lower())
# print(are_anagrams("spar", "rasp"))
# print(are_anagrams("John", "Nhot")) 

# 16.Write a function calculate_bmi(weight, height) that calculates the Body Mass Index 
	# (BMI) given weight in kilograms and height in meters.
# formular weight(kg)/height(m)^2

# def calculate_bmi(weight, height):
#         bmi = weight / int(height*2)
#         return bmi
# print(calculate_bmi(70, 1.75))

# 17.Write a function calculate_simple_interest(principal, rate, time) that calculates the 
	# simple interest given principal amount, interest rate, and time (in years).

# def calculate_simple_interest(principal, rate, time):
#     simple_interest = (principal * rate * time) / 100
#     return simple_interest
# print(calculate_simple_interest(5000, 0.2, 4))




# def get_hex_code(color):
#     for char in color:
#        if color == "red":
#         return "The hex color is #FF0000"
#        if color == "blue": 
#         return "The hex color is #FF0000"
#        if color == "green":
#          return "The hex color is #00800"
#        if color == "white":
#         return "The hex color is #FFFFF"
#     return f"unsupported color entered"

# print(get_hex_code(input("enter a color: ").lower()))