# exercise 1
# number = int(input("Enter a number: "))
# if number % 2 == 0:
#     print("True")

# else:
#     print("false")



#     # 2.
# day = input("Enter what day it is today: ")
# if day == "Wednesday":
#     print("You're correct")
# else:
#     print(f"Today is wednesday, not {day}")

    
# number = int(input("Enter a number: "))
# if number % 5 == 0:
#     print("It is a multiple of 5")
# else:
#     print("It is not a multiple of 5")


# number = int(input("Enter a number: "))
# if number % 5 == 0 and number % 3 == 0:
#     print("It is a multiple of 5")
# else:
#     print("It is not a multiple of 5")

# has_umbrella = True
# has_raincoat = False
# if has_umbrella and has_raincoat :
#     print("You are Well protected from the rain")
# elif has_umbrella:
#     print("You are proted")
# else:
#     print("You are Not protected from the rain")


# ==============================================Assignment==============================================
# 1. Collect two numbers as input from the user and assign as variables, a and b, write an if 
# statement that prints "a and b are both positive" if both a and b are positive, prints 
# "Only one is positive" if one of them is positive, and prints "Neither is positive" if 
# neither is positive.

# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))
# if a < 0 and b < 0:
#     print("a and b are both positive")
# elif a > 0 or b > 0:
#     print("only one is positive")
# else:
#     print("Neither is Positive")

# 2. Collect three numbers x, y and z as a comma separated string input from the user and print "Increasing order" if
#  they are in STRICTLY increasing order, "Decreasing order" if they are in STRICTLY decreasing order, and "Neither" otherwise.

# x = (int(input("Enter a number with : ")))
# y = (int(input("Enter a number with : ")))
# z = (int(input("Enter a number with : ")))
# if x < y < z:
#     print("Increasing order")
# elif x > y > z:
#     print("Decreasing order")
# else: 
#     print("Neither")




# 3. Write a program that reads a string called `palindrome` supplied through user input and checks if it is a palindrome.
# Print "Is a palindrome" if it is, otherwise print "Not a palindrome".

# palidrom = (input("Enter a Palindrome: "))
# if palidrom.lower().replace(" ", "") == palidrom[::-1].lower().replace(" ", ""):
#     print("Is a palindrome")
# else:
#     print("Not palindrome")

# 4. You have three variables: x, y, and z collected as 3 separate inputs from the user. Write an if statement that checks if
#  exactly two out of the three variables are equal and prints "Two are equal" if this is true. Otherwise, print "All different" or
#  "All same" accordingly.

# x = (input("Enter a number: ")).strip()
# y = (input("Enter a number: ")).strip()
# z = (input("Enter a number: ")).strip()
# if x == y == z:
#     print("All equal")
# elif x == y or z == x or y == z:
#     print("Two are equal")
# else:
#     print("All different")

# 5. Given three angles angle1, angle2, and angle3 collected as 3 separate inputs from the user, use if statements to check if 
# they can form a valid triangle. Print "Valid triangle" if the sum of the angles is 180 degrees and all angles are greater 
# than 0. Otherwise, print "Invalid triangle".

# angle1 = int(input("Enter an angle: "))
# angle2 = int(input("Enter an angle: "))
# angle3 = int(input("Enter an angle: "))

# if (angle1 > 0 and angle2 > 0 and angle3 > 0) and (angle1 + angle2 + angle3)== 180:
#     print("Valid triangle")
# else:
#     print("Invalid triangle")


# 6. You have a single character variable `ch` supplied through user input. Write an if statement that prints "Vowel" if ch 
# is a vowel (a, e, i, o, u, both uppercase and lowercase), and "Consonant" otherwise. Assume that the input is a single 
# alphabet character.

# ch = input("Enter a letters: ").strip()
# if ch.lower() in 'aeiou':
#     print("Vowel")
# else: 
#     print("Consonant")

# 7. Given a comma separated string input from the user of three colors color1, color2, and color3, write an if 
# statement to check if all three colors are primary colors (red, blue, yellow). Print "All primary colors" if 
# they are, otherwise print "Not all primary colors".

# colors1 = input("Enter a color: ")
# colors2 = input("Enter a color: ")
# colors3 = input("Enter a color: ")
# primary_color  = {"red", "blue", "yellow"}
# all_color = colors1, colors2, colors3
# if all_color == primary_color:
#     print("All primary colors")
# else:
#     print("Not all primary colors")

# 8. You have a variable `mode` supplied by the user which can be "manual", "automatic", or "off". Write an if statement
# that prints "Manual mode activated" if mode is "manual", "Automatic mode activated" if mode is "automatic", and 
# "System is off" if mode is "off".

# var_mode = input("Enter your mode: ").strip().lower()
# if var_mode == "manual":
#     print("Manual mode activated")
# elif var_mode == "automatic":
#     print("Automatic mode activated")
# elif var_mode == "off":
#     print("System is off")
# else:
#     print("invalid mode")

# 9. Given a string `message` entered by the user, use if statements to check if the message contains any of the words "urgent", 
# "important", or "immediate". If it contains any of these words, print "High priority message". Otherwise, print "Normal message".

# message = (input("Enter your message: ")).lower()
# if "urgent" in message or "important" in message or "immediate" in message:
#     print("High priority message")
# else:
#     print("Normal message")

# 10. You have two variables, status1 and status2, provided through user input, each of 
	# which can be "active", “inactive", or "pending". Write an if statement to print 
	# "Both active" if both statuses are "active", "One active" if exactly one is "active",
	# and "None active" if neither is "active".
# status1 = input("is it ('active', 'pending' or 'inactive'): ").strip().lower()
# status2 = input("is it ('active', 'pending' or 'inactive'): ").strip().lower()
# if status1 == "active" and status2 == "active":
#     print("Both active")
# elif status1 == "active" or status2 == "active":
#     print("one active")
# else:
#     print("none active")

# 11. 	Given a string `filename` supplied by the user, write an if statement to check if the
	# filename ends with “.jpg", ".png", or ".gif". Print "Image file" if it does, otherwise
	# print "Not an image file".
# filename = input("Enter your filename(.jpg, .png, .gif): ").lower()
# if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".gif"):
#     print("Image File")
# else:
#     print("Not an image file")

# 12. You have a variable `access_level` provided through user input which can be "admin",
	# "user", or "guest". Write an if statement that prints "Full access" if access_level is
	# "admin", "Limited access" if it is "user", and "No access" if it is "guest".
# access_level = input("are you a (user, admin, or guest)? ")
# if access_level == "admin":
#     print("Full access")
# elif access_level == "user":
#     print("Limited access")
# elif access_level == "guest":
#     print("No Access")
# else: 
#     print("Invalid")

# 13. Given a string `email` collected from the user, write an if statement to check if the
	# email contains both "@" and 	"." characters. Print "Valid email" if it does, otherwise
	# print "Invalid email".
# email = (input("Enter your email? "))
# if "@" in email and "." in email:
#     print("valid email")
# else:
#     print("Invalid email")


# 14. You have a variable `day` provided by user input which can be any day of the week 
	# (e.g., "Monday", "Tuesday", 	etc.). Write an if statement that prints "Weekend" if the
	# day is "Saturday" or "Sunday", and "Weekday" if it is any other day.

# day = input("What day is today(e.g., Monday, Tuesday, 	etc.)? ")
# if day == "saturday" or day == "sunday":
#     print("Weekend")
# else:
#     print("Weekdays")

# 15. Write a program that takes three numbers (num1, num2, num3) as a comma-separated string 
	# input from the user and prints the greatest number. Use conditional statements
	# to determine which number is the greatest. Bonus point if you can do it without `else` statements.

    
# num1 = (input("Enter a numbers comma seperated: ")).split(",")
# num2 = (input("Enter a numbers comma seperated: ")).split(",")
# num3 = (input("Enter a numbers comma seperated: ")).split(",")
# if num1 >= num2 and num1 >= num3:
#     highest= num1
# elif num2 >= num3 and num2 >= num1:
#     highest = num2
# elif num3 >= num1 and num3 >= num2:
#     highest = num3
# print("The highest number is", highest)


# Exercise 1: Calculate Total Sales for a Product
# Problem: A small business owner wants to calculate the total sales for a product. Ask the user to input the product name,
#  price per unit, and quantity sold, separated by commas (e.g., "T-shirt, 15, 10"). Store the input in a tuple, unpack it,
# and calculate the total sales (price × quantity). Print the product name and total sales amount.

# Hints:

# Use input() to get a comma-separated string and split it.
# Convert price and quantity to appropriate types (float for price, int for quantity).
# Unpack the tuple into variables.
# Multiply price by quantity to get total sales.

# total_sales = input("Enter the product name, price per unit, and qty sold, seperated by commas((e.g., T-shirt, 15, 10): )").split(",")
# product_name, price , qty_sold = total_sales
# total_sales1 = float(price) * int(qty_sold) 
# print("Product name:", product_name)
# print("total sale amount:$",total_sales1)
# print(tuple(total_sales))



# Exercise 2: Check Inventory Stock Status
# Problem: A store manager needs to check if an item is in stock. Prompt the user to input an item name and its current stock 
# quantity, separated by a space (e.g., "Pen 25"). Store the input in a tuple, unpack it, and print whether the item is "In Stock" 
# (quantity > 0) or "Out of Stock" (quantity = 0).

# Hints:

# Use input() and split by a space.
# Convert the quantity to an integer.
# Unpack the tuple into item and quantity.
# Use an if statement to check if quantity is 0.


# item = input("Enter item name, current stock qty, seperated by space (e.g, pen 25): ").split(" ")
# item_name, current_qty = item
# current_qty = int(current_qty)
# if current_qty == 0:
#     print("Out of stock")
# elif current_qty > 0:
#     print("In Stock")

# Exercise 3: Determine Employee Bonus Eligibility
# Problem: A company gives bonuses to employees with 5 or more years of service. Ask the user to input an employee’s name and 
# years of service, separated by a comma (e.g., "Alice, 6"). Store the input in a tuple, unpack it, and print whether the 
# employee is eligible for a bonus (years ≥ 5) or not.

# name_yearofservice = input("Enter your name and year of service, separated by a coma(e.g, Alice, 6): ").split(",")
# name, yearofservice = tuple(name_yearofservice)
# yearofservice = int(yearofservice)
# if yearofservice >= 5:
#     print("Congratulation, you are eligible for bonus")
# else:
#     print("Employee not eligible for bonus")


# Exercise 4: Check if a Customer Purchase is Discount-Eligible
# Problem: A store offers a discount for purchases over $50. Prompt the user to input the customer’s name and purchase amount, 
# separated by a space (e.g., "John 75"). Store the input in a tuple, unpack it, and print whether the customer qualifies for 
# a discount (amount > 50) or not.

# discount = input("Enter customer name and purchase amount(e.g. John 75): ").split(" ")
# name, amount = tuple(discount)
# amount = int(amount)
# if amount > 50:
#     print(f"Congratulations {name} You earn a '10%' discount of {amount}")
# else:
#     print(f"{name} you did'not qualify for discount")

# Exercise 5: Calculate Profit or Loss on a Sale
# Problem: A business owner wants to know if a sale made a profit or loss. Ask the user to input the cost price and selling price of
# an item, separated by a comma (e.g., "100, 120"). Store the input in a tuple, unpack it, and calculate the profit or loss 
# (selling price − cost price). Print whether it’s a profit, loss, or break-even (if equal)

# sales = input("Enter the cost price and selling price of item, seperated by a comma (e.g. $100, $120): ").split(",")
# cost_price, selling_price = tuple(sales)
# cost_price = int(cost_price)
# selling_price = int(selling_price)
# if cost_price < selling_price:
#     print("It a profit")
# elif cost_price == selling_price:
#     print("break-even")
# else:
#     print("It a loss")

# Exercise 6: Calculate Sales Tax and Total
# Problem: A business needs to calculate the total cost of a sale, including tax. Ask the user to input a product name, price, 
# and quantity, separated by commas (e.g., "Laptop, 500, 2"). Store the input in a tuple, unpack it, and calculate the subtotal 
# (price × quantity). Apply a 7% sales tax to the subtotal and compute the final total. Print the product, subtotal, tax amount, 
# and final total.

# sale_tax = input("product name, price,  and quantity, separated by commas (e.g., Laptop, 500, 2): ").split(",")
# product_name, price, quantity = tuple(sale_tax)
# price = float(price)
# quantity = int(quantity)
# subtotal = price * quantity
# tax_amount = 7 * subtotal / 100
# final_total = subtotal - tax_amount
# print("Product name:", product_name, "subtotal $:",subtotal, "tax amount(7%) $:", tax_amount, "final total $:", final_total)
# print(sale_tax)

# Exercise 2: Employee Shift Assignment
# Problem: A manager assigns shifts based on employee availability. Ask the user to input an employee’s name and hours available 
# per week, separated by a space (e.g., "Emma 30"). Store the input in a tuple, unpack it, and assign a shift: "Full-time" 
# (≥ 35 hours), "Part-time" (20–34 hours), or "Not Assigned" (< 20 hours). Print the employee’s name and assigned shift

# shifts = input("Enter employee's name and hours available per week, separated by a space(e.g, (Emma 30):").split(" ")
# name, hours = tuple(shifts)
# hours = int(hours)
# if hours >= 35:
#     print(f"{name} Full-time")
# elif 20 <= hours <= 34:
#     print(f" {name} Part-time")
# else:
#     print(f"{name} Not-Assigned")

# Exercise 3: Customer Feedback Rating
# Problem: A business collects customer feedback with a rating (1–5). Prompt the user to input a customer’s name and rating, 
# separated by a comma (e.g., "Lisa, 4"). Store the input in a tuple,  unpack it, and categorize the rating: "Excellent" (5), "Good" 
# (4), "Average" (3), "Poor" (2), or "Very Poor" (1). If the rating is 3 or below, add a note to follow up with the customer.

# feedback = input("Enter customers name and rating (1-5) (e.g. Lisa, 4):").split(",")
# name, rating = tuple(feedback)
# rating = int(rating)
# if rating == 5:
#    category = "Excellent"
# elif rating == 4:
#     category = "Very Good"
# elif rating == 3:
#     category = "Average"
# elif rating == 2:
#     category = "Poor"
# elif rating == 1:
#     category = "Very Poor"
# print(f"{name} Feedback: {category}")
# if rating <= 3:
#     print(f"Follow up with {name}")

# Exercise 4: Simple Break-Even Analysis
# Problem: A business owner wants to check if a product sale breaks even. Ask the user to input the product name, cost to produce, 
# and selling price, separated by commas (e.g., "Chair, 25, 30"). Store the input in a tuple, unpack it, and calculate the profit or
# loss per unit (selling price − cost). If profit is positive, print "Profit"; if negative, print "Loss"; if zero, print "Break-even".
# Also, print the profit/loss amount per unit.
    
# analysis = input("Enter product name, cost to produce, and selling price (e.g. Chair, 25, 30): ").split(",")
# product, cost_p, selling_p = tuple(analysis)
# profit = float(selling_p) - float(cost_p)
# if profit > 0:
#     print(f"{product}, Profit: {profit}")
# elif profit < 0:
#     print(f"{product}, Loss: {profit}")
# else:
#     print(f"{product}, Break-even: {profit}")



# Exercise 5: Track Daily Sales Goal
# Problem: A store has a daily sales goal of $200. Prompt the user to input two product names and their sales amounts, separated by
# commas (e.g., "Coffee, 80, Tea, 150"). Store the input in a tuple, unpack it, and calculate the total sales. Print whether the total
# meets, exceeds, or falls short of the $200 goal, and by how much.

# sales_goals = input("Enter two product name and sales amounts (e.g. Coffee, 80, Tea, 150): ").split(",")
# product1, price1, product2, price2 = tuple(sales_goals)
# total_sales = float(price1) + float(price2)
# difference = int(total_sales) - 200
# if total_sales == 200:
#    print(f"meets $200 goal by ${difference}")
# elif total_sales > 200:
#     print(f"exceeds $200 goal by ${difference}")
# elif total_sales < 200:
#     print(f"falls short $200 goal by ${difference}")

# Exercise 6. Proocess Multiple Sales with Tax and Discount
# Problem: A store applies a 5% discount on total sales over $100 and a 7% sales tax. Prompt the user to input two product sales 
# as a comma-separated string (e.g., "Shirt, 50, 2, Pants, 30, 3"), where each product has a name, price, and quantity. Store the 
# data in a tuple of tuples, unpack it, and calculate the subtotal for each product (price × quantity). Apply the discount if the 
# total subtotal exceeds $100, then add tax. Print each product’s subtotal, the discount (if any), tax, and final total.

# sales = input("Enter two product sales (e.g., shirt, 50, 2, pants, 30, 3): ").split(",")
# product1, price1, qty1, product2, price2, qty2 = tuple(sales)
# subtotal = float(price1) * int(qty1) + float(price2) * int(qty2)
# subtotal_discout  = subtotal * 5 / 100
# product1_subtotal = float(price1) * int(qty1)
# product2_subtotal = float(price2) * int(qty2)
# tax = 7 * subtotal / 100
# if subtotal >= 100 - subtotal_discout and subtotal + tax:
#     print(f"product one subtotal: {product1_subtotal}, product two subtotal: {product2_subtotal}, total discount(5%): {subtotal_discout},  tax(7%): {tax} Final total for product 1 and 2 : {subtotal - subtotal_discout + tax}")
# elif subtotal < 100: 
#     print(f"product one subtotal: {product1_subtotal}, product two subtotal: {product2_subtotal}, total discount: No discount for sale, tax(7%): {tax}, Final total for product 1 and 2 : {subtotal + tax}")

# Exercise 2: Employee Overtime Pay Calculator
# Problem: A company pays employees $20/hour for regular hours (≤ 40) and $30/hour for overtime (> 40). Ask the user to input two 
# employees’ names and hours worked, separated by commas (e.g., "Alice, 45, Bob, 30"). Store the data in a tuple of tuples, unpack 
# it, and calculate each employee’s pay. Print each employee’s regular pay, overtime pay (if any), and total pay.

# work_info = input("Enter two employees' names and hours worked (e.g. Alice, 45, Bob, 30): ").split(",")
# employee1, hours1, employee2, hours2 = tuple(work_info)
# regular_hours1 = int(hours1) * 20
# regular_hours2 = int(hours2) * 20
# overtime_hours1 = int(hours1) * 30
# overtime_pay1 = overtime_hours1 - regular_hours1
# overtime_hours2 = int(hours2) * 30
# overtime_pay2 = overtime_hours2 - regular_hours2

# if int(hours1) > 40 and int(hours2) > 40:
#     print(f"Employee name one: {employee1}, hours: {hours1}, Overtime pays ($): {overtime_pay1}, Total pay ($): {overtime_hours1}, Employee name two: {employee2}, hours: {hours2}, Overtime pay2 ($): {overtime_pay2}, Total pay two ($): {overtime_hours2}")
# elif int(hours1) < 40 and int(hours2) < 40:
#     print(f"Employee name one: {employee1}, hours: {hours1}, Overtime pays ($): None, Total pay ($): {regular_hours1}, Employee name two: {employee2}, hours: {hours2}, Overtime pay2: None, Total pay two ($): {regular_hours2}")
# elif int(hours1) > 40 and int(hours2) < 40:
#     print(f"Employee name one: {employee1}, hours: {hours1}, Overtime pays ($): {overtime_pay1}, Total pay ($): {overtime_hours1}, Employee name two: {employee2}, hours: {hours2}, Overtime pay2: None, Total pay two ($): {regular_hours2}")
# elif int(hours1) < 40 and int(hours2) > 40:
#     print(f"Employee name one: {employee1}, hours: {hours1}, Overtime pays ($): None, Total pay ($): {regular_hours1}, Employee name two: {employee2}, hours: {hours2}, Overtime pay2: {overtime_pay2}, Total pay two ($): {overtime_hours2}")


# Exercise 3: Customer Order Status Tracker
# Problem: A business tracks customer orders with a status based on total cost. Ask the user to input two orders as a comma-separated 
# string (e.g., "Order1, 120, Order2, 80"), where each order has a name and total cost. Store in a tuple of tuples, unpack it, and
#  assign a status: "High Priority" (cost ≥ 100), "Standard" (50 ≤ cost < 100), or "Low Priority" (< 50). Print each order’s name,
#  cost, and status, and count how many orders are High Priority.

# orders = input("input two orders (e.g., order1, 120, order2, 80): ").split(",")
# order_name1, cost1, order_name2, cost2 = tuple(orders)
# total_cost = float(cost1) + float(cost2)
# if total_cost >= 100:
#     print(f"order info: {list(orders)}, High Priority")
# elif 50 <= total_cost < 100:
#     print(f"order info: {list(orders)}, Standard Priority")
# else:
#     print(f"order info: {list(orders)}, Low Priority")

# Exercise 4: Inventory Restock Alert
# Problem: A store needs to monitor inventory levels. Prompt the user to input three items, each with a name and quantity, separated
#  by commas (e.g., "Pen, 5, Notebook, 20, Eraser, 2"). Store in a tuple of tuples, unpack it, and check each item’s quantity 
#  a restock threshold of 10. Print each item’s name, quantity, and whether it needs restocking (quantity < 10). Also, print the total 
#  number of items needing restocking.


# items = input("input three items each with a name and qty (e.g., Pen, 5, Notebook, 20, Eraser, 2.): ").split(",")
# item1, qty1, item2, qty2, item3, qty3 = tuple(items)
# need_restock1 = int(qty1) < 10
# need_restock2 = int(qty2) < 10
# need_restock3 = int(qty3) < 10
# qty1, qty2, qty3 = int(qty1), int(qty2), int(qty3)
# if qty1 < 10 and qty2 < 10 and qty3 < 10:
#     print(f"items and quantity : {tuple(items)}, All Items Need restock")
# elif qty1 > 10 and qty2 > 10 and qty3 > 10:
#      print(f"items and quantity : {tuple(items)}, No Items Need restock")
# elif qty1 > 10 and qty2 < 10 and qty3 > 10:
#      print(f"items and quantity : {tuple(items)}, Only Items two {item2} need restock")
# elif qty1 > 10 and qty2 < 10 and qty3 < 10:
#      print(f"items and quantity : {tuple(items)}, Items two and item three {item2}, {item3} need restock")
# elif  qty1 < 10 and qty2 > 10 and qty3 > 10:
#      print(f"items and quantity : {tuple(items)}, Only Items one {item1} need restock")
# elif qty1 < 10 and qty2 < 10 and qty3 > 10:
#      print(f"items and quantity : {tuple(items)}, Items one and item two {item1}, {item2} need restock")
# elif  qty1 > 10 and qty2 > 10 and qty3 < 10:
#      print(f"items and quantity : {tuple(items)}, Only Items three {item3} need restock")
# elif qty1 < 10 and qty2 > 10 and qty3 < 10:
#      print(f"items and quantity : {tuple(items)}, Items one and item three {item1}, {item3} need restock")
     

     
# items = input("input three items each with a name and qty (e.g., Pen, 5, Notebook, 20, Eraser, 2.): ").split(",")
# item1, qty1, item2, qty2, item3, qty3 = tuple(items)
# qty1, qty2, qty3 = int(qty1), int(qty2), int(qty3)

# need_restock = []

# if qty1 < 10:
#     need_restock.append(item1)

# if qty2 < 10:
#     need_restock.append(item2)

# if qty3 < 10:
#     need_restock.append(item3)


# print(f"Item: {item1}, qty: {qty1}, needs restocking: {item1 in need_restock}")
# print(f"Item: {item2}, qty: {qty2}, needs restocking: {item2 in need_restock}")
# print(f"Item: {item3}, qty: {qty3}, needs restocking: {item3 in need_restock}")

# print(f"Total number of items that need restocking: {len(need_restock)}")


# Exercise 5: Budget Allocation for Expenses
# Problem: A small business allocates a budget across expenses. Ask the user to input two expense categories, their amounts, and a 
# total budget, separated by commas (e.g., "Rent, 500, Food, 300, 1000"). Store in a tuple (categories and amounts as a tuple of 
# tuples, budget as a separate value). Unpack the data, calculate the total expenses, and check if they’re within budget. If over 
# budget, suggest reducing the larger expense by the excess amount. Print the status and details.

# expenses = input("input two expense categories, their amounts, and a total budget(e.g. Rent, 500, Food, 300, 800):").split(",")
# exp1, amnt1, exp2, amnt2, total = tuple(expenses)
# tuple(expenses) == tuple(exp1), float(amnt1), tuple(exp2), float(amnt2), float(total)
# total_exp = float(amnt1) + float(amnt2)
# excess_amount = float(total_exp) - float(total)
# if total_exp < float(total):
#     print(f"Expenses: {tuple(expenses)}, Total expenses($): {total_exp}, Within Budget of ($): {float(total)},")
# elif total_exp > float(total) and float(amnt1) > 500:
#      print(f"Expenses: {tuple(expenses)}, Total expenses($): {total_exp}, Over Budget of ($): {float(total)}, over budget by($): {float(total_exp) - float(total)}, suggestion: Reduce($){float(total_exp) - float(total)} from {exp1}")
# elif total_exp > float(total) and float(amnt2) > 500:
#     print(f"Expenses: {tuple(expenses)}, Total expenses($): {total_exp}, Over Budget of ($): {float(total)}, over budget by($): {float(total_exp) - float(total)}, suggestion: Reduce($){float(total_exp) - float(total)} from {exp2}")

# Exercise 1: Freelancer Invoice Generator
# Problem: A freelancer needs to generate an invoice for two clients. Prompt the user to input two client projects as a 
# comma-separated string (e.g., "Logo Design, 50, 10, Website, 75, 20"), where each project has a project name, hourly rate, 
# and hours worked. Store the data in a tuple of tuples, unpack it, and calculate the total fee for each project (rate × hours). 
# Apply a 10% late fee if the hours exceed 15. Print each project’s details, including any late fee, and the total invoice amount.

# invoice = input("input two client projects(e.g., Logo Design, 50, 10, Website, 75, 20): ").split(",")
# project1, hr1, hr_work1, project2, hr2, hr_work2 = tuple(invoice)
# project1_totalfee = float(hr1) * float(hr_work1)
# project2_totalfee = float(hr2) * float(hr_work2)
# latefee_project1 = []
# latefee_project2 = []
# # total_amount1 = float(latefee_project1) + float(project1_totalfee)
# # total_amount2 = float(latefee_project2) + float(project2_totalfee)

# if float(hr_work1) > 15:
#     latefee_project1.append(10 * project1_totalfee/100)
# if float(hr_work2) > 15:
#     latefee_project2.append(10 * project2_totalfee/100)

# print(f"project name: {project1}, hourly-rate: {hr1}, hours work: {hr_work1}, Late fee: {float(latefee_project1)}, Total invoice amount: {project1_totalfee + float(latefee_project1)}")
# print(f"project name: {project2}, hourly-rate: {hr2}, hours work: {hr_work2}, Late fee: {float(latefee_project2)}, Total invoice amount: {project2_totalfee + float(latefee_project2)}")








