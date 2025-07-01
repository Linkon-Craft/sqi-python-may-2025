# is_raining = False

# if is_raining:
#     print("Carry an umbrella")
# else:
#     print("Enjoy the outdoors")


# num1 = 5
# num2 = 12

# print(num1 > num2)

# if num1 > num2:
#     print("num1 is greater than num2")
# else:
#     print("num1 is not greater than num2")


# num1 = 5
# num2 = 12


# if num1 > num2:
#     print("num1 is greater than num2")
# elif num1 < num2:
#     print("num1 is less than num2")
# else:
#     print("num1 is equal to num2")

# num1 = 5
# num2 = 12


# if num1 > num2:
#     print("num1 is greater than num2")
# elif num1 < num2:
#     print("num1 is less than num2")
# elif num1 == num2:
#     print("num1 is equal to num2")


# Exercise 1
# Ask the user to enter a number and print True if the number is even, otherwise, print False

# number = int(input("Enter a number to check if it is even: "))

# if number % 2 == 0:
#     print(True)    
# else:
#     print(False)    


# Exercise 2
# Ask the user to enter what day it is today, if they enter Wednesday, print "You are correct",
# otheriwse, print, "Today is Wednesday, not `day`"

# today = input("What day is it today?: ")
# if today == "Wednesday":
#     print("You are correct")
# else:
#     print(f"Today is Wednesday, not {today}")



# Ask the user to enter a positive number and print True if the number is even, otherwise, print False.
# If the number is negative, print "Enter a positive number"


# number = int(input("Enter a number to check if it is even: "))

# if number % 2 == 0 and number > 0:
#     print("Positive even number")
# elif number % 2 != 0 and number > 0:
#     print("Positive odd number")
# else:
#     print("Negative number")

# number = int(input("Enter a number to check if it is even: "))


# if number < 0:
#     print("Negative number")
# elif number % 2 == 0:
#     print("Positive even number")
# elif number % 2 != 0:
#     print("Positive odd number")


# Ask the user for a number, 
# if the number is a multiple of 5, print "It is a multiple of 5",
# otherwise, print("It is not a multipole of 5")

# num = int(input("Enter a number: "))
# if num % 5 == 0:
#     print("It is a multiple of 5")
# else:
#     print("It is not a multiple of 5")


# Ask the user for a number, 
# if the number is a multiple of 3 and 5, print "It is a multiple of  3 and 5",
# otherwise, print("It is not a multipole of 3 and 5")

# number = int(input("Enter a number: "))

# if number % 3 == 0 and number % 5 == 0:
# # if number % 15 == 0:
#     print("It is a multiple of 3 and 5")
# else:
#     print("It is not a multiple of 3 and 5")


# If the number is amultiple of both 3 and 5, print It is a multiple of both 3 and 5
# If the number is only a multiple of 3, print "It is a multiple of 3"
# If the number is only a multiple of 5, print "It is a multiple of 5"

# number = int(input("Enter a number: "))

# # if number % 3 == 0 and number % 5 == 0:
# if number % 15 == 0:
#     print("It is a multiple of 3 and 5")
# elif number % 3 == 0:
#     print("It is a multiple of only 3")
# elif number % 5 == 0:
#     print("It is a multiple of only 5")
# else:
#     print("It is not a mutiple of 3, 5 or 15")




# truthy and falsy values in conditional statements

# Assuming the user may enter invalid chars (i.e. not just alphabets and/or spaces)

# name = input("Enter your name: ").strip()

# import string

# allowed_chars = set(string.ascii_letters)
# allowed_chars.add(" ")
# print(allowed_chars)
# name_chars = set(name)
# print(name_chars)

# if not name:
#     print(f"Good morning, Anonymous 🌻")
# elif name_chars.issubset(allowed_chars):
#     print(f"Good morning, {name} 🌻")
# else:
#     print(f"Invalid chars in name, enter only alphabets and spaces")




# Assuming the user only enters valid chars (i.e. alphabets and/or spaces)
# name = input("Enter your name: ").strip()
# if not name:
#     print("Good morning, Anonymous 🌻")
# else:
#     print(f"Good morning, {name} 🌻")


# has_umbrella = False
# has_raincoat = False

# if the user has an umbrella, then print "You are protected from the rain"
# if the user has a raincoat, then print "You are protected from the rain"
# If the user has both, print "You are WELL protected from the rain"
# If the user has none, print "You are NOT protected from the rain"

# DRY -> Don't Repeat Yourself

# if has_umbrella and has_raincoat:
#     print("You are WELL protected from the rain")
# elif has_umbrella or has_raincoat:
#     print("You are protected form the rain")
# else:
#     print("you are not protected from the rain")


# ternary operator

# is_raining = False

# if is_raining:
#     print("Carry an umbrella")
# else:
#     print("Enjoy the outdoors")

# is_raining = False

# print("Carry an umbrella") if is_raining else print("Enjoy the outdoors")

# print("Carry an umbrella" if is_raining else "Enjoy the outdoors")



# is_raining = False

# if is_raining:
# advice = "Carry an umbrella"
# else:
#     advice = "Enjoy the outdoors"

# print(advice)


# is_raining = False

# advice = "Carry an umbrella" if is_raining else "Enjoy the outdoors"
# print(advice)



# SILICON VALLEY

# FAANG -> Facebook, Amazon, Apple, Netflix, Google