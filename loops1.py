# Print "I love Python" 10 times


# num = 7
# while num <= 50:
#     print(num )
# num += 2

# i = 0
# while i <= 200:
#     print(i)
# i += 2



# i = 69
# while i <= 283:
#     if i % 5  == 0 and i % 3 == 0:
#         print(i)
#     i += 1

# numbers = []
# i = 1
# while i <= 50:
#     numbers.append(i)
#     i += 1
# print(numbers)


# i = 1
# while i <= 10:
#     if i != 5:
#         print(i)
#     i += 1



# length = int(input("Enter a number: "))
# breadth = int(input("Enter a number: "))
# i = 1
# while i <= breadth:
#     print("*" * length)
#     i += 1


# series = ["wednesday", "Umbrella Academy", "Vampire Diaries", "Stranger Things", "Blacklist", "Blindspot", "Prison Break"]

# i = 0
# while i <= len(series):
#     print(f"series {i}: {series[i]}")
#     i += 1


# print the first 10 multiple of 5

# multiple_of_5 = []

# i = 5
# while True:
#     multiple_of_5 != 50
    



# i = 1

# while i <= 10:
#     print(f"{i}). I love Python")
#     i += 1


# i = 20
# while i < 41:
#     print(i)
#     i += 1


# num = 40
# while num >= 20:
#     print(num)
#     num -= 1

# count all the even numbers from 7 to 50

# i = 7
# while i <= 50:
#     print(i+1)
#     i += 2

# i = 7
# while i <= 50:
#     print("something")
#     if i % 2 == 0:
#         print(i)
#     i += 1

# print all the numbers that are multiples of 5 between 1 and 200


# Count from 1 to 50

# i = 1
# while i < 51:
#     print(i)
#     i += 1



# Count all the odd numbers from 1 to 67
# i = 1
# while i < 68:
#     print(i)
#     i += 2

# Count all the odd numbers from 2 to 67
# i = 2
# while i < 68:
#     print(i + 1)
#     i += 2 

# i = 2
# while i < 68:
#     if i % 2 != 0:
#         print(i)
#     i += 1


# print the numbers that are both multiples of 3 and 5 between 69 and 203
# i = 69
# while i <= 203:
#     if i % 15 == 0:
#         print(i)
#     i += 1



# print a list of the numbers that are both multiples of 3 and 5 between 69 and 203
# i = 69
# while i <= 203:
#     multiples_of_15 = []
#     if i % 15 == 0:
#         multiples_of_15.append(i)
#     i += 1


# print(multiples_of_15)

# while loop exercises

# count from 1 to 50, and print a comma separated string of the numbers
# your output will look like:
# "1, 2, 3, 4, ..., 45, 46, 47, 48, 49, 50"

# numbers = []
# i = 1
# while i <= 50:
#     numbers.append(str(i))
#     i += 1


# print(numbers)
# print(", ".join(numbers))


# count from 1 to 50, and print a comma separated string of the numbers
# don't use a list


# numbers = ""
# i = 1
# while i <= 50:
#     numbers += str(i)
#     if i < 50:
#         numbers += ", "
#     i += 1


# print(numbers)
# names = "Awwal, Lekan"
# print(names)
# # add Omolola 
# # add Molayo
# # names = names + ", Omolola"
# names += ", Omolola"
# names += ", Molayo"
# print(names)

# Print numbers from 1 to 10, but skip number 5
# Expected Output:
# 1
# 2
# 3
# 4
# 6
# 7
# 8
# 9
# 10

# i = 1
# while i <= 10:
#     if i != 5:
#         print(i)
#     i += 1


# Print a square of stars
# Ask the user to enter a number
# Example 1:
# Input: 3

# Output:
# ***
# ***
# ***

# Example 2:
# Input: 5

# Output:
# *****
# *****
# *****
# *****
# *****


# 1. Collect the number from the user
# 2. Multiply the * by the number the user enters
# 3. Repeat that `length` times


# length = int(input("Enter a number: "))
# i = 1
# while i <= length: 
#     print("*" * length)
#     i += 1


# Print a rectangle of area length X breadth
# ask the user to provide length and breadth
# Example:
# Input:
# Length: 5
# Breadth: 4
# *****
# *****
# *****
# *****


# 1. Collect the length and breadth of the rectangle
# 2. Print `length`` stars
# 3. Repeat number 2 `breadth`` times

# length = int(input("Enter the length of the rectangle: "))
# breadth = int(input("Enter the breadth of the rectangle: "))

# i = 1
# while i <= breadth:
#     print("*" * length)
#     i += 1



# Print "1" ten times on the same line using a while loop
# Expected Output:
# 1111111111

# result = ""
# i = 1
# while i <= 10:
#     result += "1"
#     i += 1

# print(result)


# result = []
# i = 1
# while i <= 10:
#     result.append("1")
#     i += 1

# print("".join(result))


# break and cointinue
# Print numbers from 1 to 10, but skip number 5
# Expected Output:
# 1
# 2
# 3
# 4
# 6
# 7
# 8
# 9
# 10

# i = 0
# while i < 10:
#     i += 1
#     if i == 5:
#         continue
#     print(i)



# print all even numbers form 1 to 20

# i = 1
# while i <= 20:
#     i += 1
#     if i % 2 != 0:
#         continue
#     print(i)


# print all the numbers from 5 to 20, but stop once you reach a multiple of 15

# i = 5
# while i <= 20:
#     if i % 15 == 0:
#         break
#     print(i)
#     i += 1


# how to loop through strings, lists with while loops
# name = "Winnie"

# print(name[0])  # 0
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])
# print(name[5])  # 5

# i = 0
# # while i <= len(name) - 1:
# while i < len(name):
#     char = name[i]
#     print(char)
#     i += 1

# name = "Omolola"

# i = 0
# while i < len(name):
#     char = name[i]
#     print(char)
#     i += 1


# ATM withdrawal simulation


# directions = ["up", "down", "left", "right"]

# i = 0
# while i < len(directions):
#     direction = directions[i]
#     print(direction)
#     i += 1



# items = ("cap", "shoe", "basket")
# i = 0
# while i < len(items):
#     item = items[i]
#     print(item)
#     i += 1



# series = ["Wednesday", "Umbrella Academy", "Vampire Diaries", "Stranger Things", "Blacklist", "Blindspot", "Prison Break"]

# Output:
# Series 1: Wednesday
# Series 2: Umbrella Academy
# Series 3: Vampire Diaries
# Series 4: Stranger Things
# Series 5: Blacklist
# Series 6: Blindspot
# Series 7: Prison Break

# Output:
# The series at index 0 is Wednesday
# The series at index 1 is Umbrella Academy

# i = 0
# while i < len(series):
#     print(f"Series {i+1}: {series[i]}")
#     i += 1


# i = 0
# while i < len(series):
#     print(f"The series at index {i}: {series[i]}")
#     i += 1


# series = ["Wednesday", "Umbrella Academy", "Vampire Diaries", "Stranger Things", "Blacklist", "Blindspot", "Prison Break"]

# Output:
# The series at index 0 is Wednesday
# The series at index 1 is Umbrella Academy
# The series at index 2 is Vampire Diaries
# The series at index 3 is Stranger Things
# The series at index 4 is Blacklist
# The series at index 5 is Blindspot
# The series at index 6 is Prison Break


# i = 0
# while i < len(series):
#     print(f"The series at index {i} is {series[i]}")
#     i += 1


# count = 0
# while True:
#     print("something")
#     count += 1
#     if count == 5:
#         break





# print the first 10 multiples of 5, don't include 50 anywhere in your code.

# count = 0
# i = 5
# while count < 10:
#     if i % 5 == 0:
#         print(i)
#         count += 1
#     i += 1


# count = 0
# i = 5
# while True:
#     if i % 5 == 0:
#         print(i)
#         count += 1
#     if count == 10:
#         break
#     i += 1

    

# Assignment: print a list of the first 12 multiples of 3

# Write a program that simulates an ATM withdrawal process. The user should enter their 
# balance and then enter withdrawal amounts until they decide to stop. Ensure the user does
# not withdraw more than their balance.
# Sample Input and Output:
# Enter your balance: 500
# Enter withdrawal amount: 100
# Remaining balance: 400
# Do you want to make another withdrawal? (yes/no): yes
# Enter withdrawal amount: 50
# Remaining balance: 350
# Do you want to make another withdrawal? (yes/no): no
# Final balance: 350

# balance = int(input("Enter your balance: "))
# while True:
#     withdrawal_amount = int(input("Enter withdrawal amount: "))
#     if withdrawal_amount > balance:
#         print("Insufficient funds!")
#         continue

#     balance -= withdrawal_amount
#     print(f"Remaining balance: {balance}")

#     continue_withdrawal = input("Do you want to make another withdrawal? (yes/no): ").strip().lower()

#     if continue_withdrawal == "yes":
#         continue
#     print(f"Final balance: {balance}")
#     break


# balance = int(input("Enter your balance: "))
# main_loop = True
# while main_loop:
#     withdrawal_amount = int(input("Enter withdrawal amount: "))
#     if withdrawal_amount > balance:
#         print("Insufficient funds!")
#         continue

#     balance -= withdrawal_amount
#     print(f"Remaining balance: {balance}")

#     keep_asking = True
#     while keep_asking:
#         continue_withdrawal = input("Do you want to make another withdrawal? (yes/no): ").strip().lower()

#         if continue_withdrawal == "yes":
#             keep_asking = False
#             continue
#         if continue_withdrawal == "no":
#             print(f"Final balance: {balance}")
#             main_loop = False
#             break
#         print("Invalid input")
        
