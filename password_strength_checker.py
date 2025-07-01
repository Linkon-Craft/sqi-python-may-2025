# Write a program in a file named `password_strength_checker.py` that takes a string called `password` and prints `True` if the password is strong and `False` otherwise. A strong password:

# Is at least 8 characters long.
# Contains both uppercase and lowercase characters.
# Contains at least one digit.
# Contains at least one special character (e.g., !@#$%^&*()).

# password = "p@sswoRd"
# at_least_8_chars = len(password) >= 8

# has_upper = any(char.isupper() for char in password)
# has_lower = any(char.islower() for char in password)

# print(all([at_least_8_chars, has_upper, has_lower]))
# print(at_least_8_chars and has_upper and has_lower)


# Question 1: Username Validator
# Problem: Write a program in a file named username_validator.py that takes a string called username and prints True if the username
#  is valid, False otherwise. A valid username:

# Is 4–12 characters long.
# Contains only letters, digits, or underscores (_).
# Starts with a letter.
# Expected Behavior:

# Input: john_doe123 → Output: True
# Input: 123user → Output: False

# Hints:

# Check length with len().
# Use a loop to check each character is a letter, digit, or underscore (use strings like "abcdefghijklmnopqrstuvwxyz" for letters).
# Check the first character separately to ensure it’s a letter.
# Use a flag to track validity.


username = (input("Enter your Username: " )).strip().lower()

for char in username:
    if  4 < len(username) <= 12:
        username == True
        print(username)

    if  username.startswith("abcdefghijklmnopqrstuvwxyz"):
        username == True
        print(username)

    if "0123456789" in username:
        username == True
        print(username)

    if "_" in username:
        username == True
        print(username)

    else:
        username == False
        print("Invalid Input")
        continue

    









# def base_exponent(base, exponent):
#     print(f"{base}^{exponent}= {base ** exponent}")

# base_exponent(2, 4)


# def multiply_nums(num1, num2):
#     return f"{num1} * {num2} = {num1 * num2}"
# result = multiply_nums(3, 5)
# print(result)

# def square_num(num):
#     return num * num
# num = square_num(3)
# print(num)

# def is_even(num):
#     if num % 2 == 0:
#         return True
    
# num = is_even(5)
# print(num)


# def uppercase_all_names(*names):
#     return[name.upper() for name in names]
# print(uppercase_all_names())


# def filter_out_nums_less_than_50(*nums):
#     return tuple([num for num in nums if num > 50])
# print(filter_out_nums_less_than_50(20, 534, 30, 55, 70))


# def is_alliteration(two_word_string):
#     return[word for word in two_word_string if True]
# two_word_string =


# List of questions (each is a dictionary with question, options, and correct answer)


# List of target words to check for
# words_to_check = ["python", "code", "function", "loop"]

# user_text = input("Enter a sentence: ")

# # Call the function
# matched_count = count_words_in_input(words_to_check, user_text)

# print(f"{matched_count} word(s) from the list were found in your input.")



# word_list = ["apple", "banana", "orange"]
# def match_words():
#     user_input = input("Enter a sentence")
#     count = 0
# result = count_matching_words(word_list, user_input)
# print("Matched words count:", result)




# "I like to eat banana and apple every day"