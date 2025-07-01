# Ask the user for their age
# If they enter a negative age, keep asking till they enter a valid age
# When you have a valid age, tell them what year they were born

# from datetime import datetime

# current_year = datetime.now().year
# while True:
#     try:
#         age = int(input("Enter your age: "))
#     except ValueError:
#         print("Enter a valid number")
#     except Exception:
#         print("Something went wrong")
#     else:
#         if age < 1:
#             print("Negative ages are not allowed")
#             continue
#         print(f"You were born in {current_year - age}")
#         break

# class NegativeAgeError(Exception):
#     def __init__(self, message):
#         self.message = message
#         super().__init__(self.message)


# from datetime import datetime

# current_year = datetime.now().year
# def calculate_birth_year():
#     while True:
#         try:
#             age = int(input("Enter your age: "))
#         except ValueError:
#             print("Enter a valid number")
#         except Exception:
#             print("Something went wrong")
#         else:
#             if age < 1:
#                 raise NegativeAgeError("Negative ages are not allowed")
#             print(f"You were born in {current_year - age}")
#             break


# try:
#     calculate_birth_year()
# except NegativeAgeError as e:
#     print(f"Negative age entered: {e}")


# Write a function divide(num1, num2) and returns the result of the division

# def divide(num1, num2):
#     try:
#         result = float(num1) / float(num2)
#     except ZeroDivisionError as e:
#         return f"Cannot divide by zero: {e}"
#     except ValueError as e:
#         return f"num1 and num2 must be numbers: {e}"
#     except TypeError as e:
#         return f"num1 and num2 must be numbers: {e}"
#     finally:
#         print("This block will always run")
#     return f"The result is {result}"

# print(divide("4", "23whbdujenfd"))




# Assignment 
# Define a custom exception called NegativeNumberError.
# Write a function check_positive(number) that raises 
# NegativeNumberError if the input number is negative.
# Catch the exception when calling the function.

# class NegativeNumberError(Exception):
#     pass
          

# def check_positve():
#     while True:
#         try:
#             number = int(input("Enter a number: "))
#         except ValueError as e:
#             return f"Input must be a number: {e}"
#         except TypeError as e:
#             return f"Input must me a number: {e}"
#         else:
#             if number < 1:
#                 raise NegativeNumberError(f"Negative number are not allowed")
#             break

# try:
#     check_positve()
# except NegativeNumberError as e:
#      print(f"Error: {e}")


    

# 2. Handle Multiple Exceptions:
# Write a function safe_divide(a, b) that performs division.
# Handle ZeroDivisionError if the divisor is zero.
# Handle TypeError if the inputs are not numbers.
# Handle ValueError if the inputs are not convertible to floats.


# def safe_divide(a, b):
#     while True:
#         try:
#             result = float(a) / float(b)
#         except TypeError as e:
#             return f"Input are not numbers: {e}"
#         except ValueError as e:
#             return f"Inputs are not convertible to floats: {e}"
#         except Exception as e:
#             return f"Something went wrong: {e}"
#         except ZeroDivisionError as e:
#             return f"Number cannot be zero: {e}"
#         finally:
#             print(f"The block will always run")
#         return f"The result is {result}"
    
# print(safe_divide(9, 0))
