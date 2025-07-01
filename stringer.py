"""
This module will explain strings to SQI 2025 MAy COHORT
"""

# Create a variable `text` that contains "today is Monday"
# Capitalize the text.
# Turn the text to lowercase
# Turn the text to uppercase
# Check if text starts with "T" regardless of the case of `text`
# Check if text ends with "Day" regardless of the case of `text`


# text = "today is Monday"
# print(text.capitalize())
# print(text.lower())
# print(text.upper())
# print(text.upper().startswith("T"))

# print(text.upper().endswith("Day".upper())) 
# print(text.upper().endswith("DAY")) 
# print(text.upper())
# print("Day".upper())

# tuple_t = ("T", "t")
# print(text.startswith(tuple_t))
# print(text.startswith(("T", "t")))


# name = "Omolola"
# print(name.lower().startswith("o"))



# my_list = ["Joy", "Happiness", "Sadness", "Charity", "Peace", "Chaos"]

# my_tuple = ("TV", "Radio", "Fryer", "Washing Machine", "Jug")

# # print(my_list[2])
# # print(my_tuple)

# # my_list.append("Serenity")
# my_tuple.append("Serenity")
# print(my_list)

# split, join, count, find, index, islower, isupper, strip, replace


# greeting = "Hello Hello"
# print(greeting.count("l"))
# print(greeting.count("z"))
# print(greeting.lower().count("h"))
# print(greeting.count("Hello"))




# magic_phrase = "abracadabra"
# # print(len(magic_phrase))  # 11
# print(magic_phrase.count("abra"))  # 2
# print(magic_phrase.count("ab"))  # 2


# text = "abababa"
# print(text.count("ab"))
# print(text.count("ba"))
# print(text.count("aba"))


# text = "today is Monday"
# uppercase = text.upper()
# print(uppercase)
# print(text)

# text = "today is Monday"
# text = text.upper()  # 
# print(text)



# text = "abababa"
# print(text.find("b")) 
# print(text.find("a", 2)) 
# print(text.find("b", 2)) 


# text = "today is Monday"
# print(text.find("Monday")) 
# print(text.find("day"))
# print(text.find("day", 5))
# print(text.find("Tuesday")) 
# print(text.find("wegvhnmf,")) 


# text = "today is Monday"
# print(text.index("today"))
# print(text.index("is"))
# print(text.index("Tuesday"))


# name = "Molayo"
# print(name.islower())
# print(name.isupper())
# print(name.upper().isupper())
# name = "molayo"
# print(name.upper().isupper())
# print(name.isupper())
# print(name.islower())


# story = "\tOnce upon a time  "
# print(story.lstrip())
# print(story.rstrip())
# print(story.strip())


# story = "***Once upon a time***********"
# print(story.lstrip("*"))
# print(story.rstrip("*"))
# print(story.strip("*"))

# story = "***Once upon a time***********"
# story = "   Once upon a time "
# print(story.replace(" ", ""))
# print(story.upper().replace("O", "P"))
# print(story.replace("time", "day").replace("upon", "UPON"))
# print(story.replace("Z", "P"))


# story = "Once upon a time"
# print(story.split())
# story = "Once*upon*a*time"
# print(story.split())
# print(story.split("*"))

# movies = "Love in every word, Beauty in Black, My Siblings and I, Black Diamond, Mission Impossible"
# print(movies.split(", "))

# games = ["CandyCrush", "KillerBean", "DreamLeague", "LoveParadise", "SubwaySurf", "Watchdog"]

# print("".join(games))
# print(" ".join(games))
# print(", ".join(games))

# 17 - 44



# pep 8 -> style guide for Python


# docstring -> documentation string


# !!!!BAD
"""
a  = 6
b  = 4
print(a + b)  # add a and b together
"""


from datetime import datetime

# Assignment
# 17. 
name = "James John Kennedy"
print(name.split())

# 18. 
cities_list = ['New York', 'Los Angeles', "Chicago"]
print(" ; ".join(cities_list))
# cities_string = 'New York' Los Angeles' Chicago'



19.
sentence = "the quick brown fox jumps over the lazy dog"
print(sentence.capitalize())

20.
book_title = "to kill a mockingbird"
capitalize_text = book_title.title()
print(capitalize_text)

21. 
text = "Hello World"
print(text.count("o"))

22.
filename = "documents.txt"
print(filename.startswith("doc"))

23.
url = "https://www.example.com"
print(url.endswith(".com"))

24.
phrase = "find the needle in the paystack"
print(phrase.find("needle"))

25.
template = "Hello, {}. Welcome to {}."
print(template.format("Alice", "Wonderland"))

26.
quote = "To be or not to be"
print(quote.find("not"))

27.
word = "hello"
print(word.islower())

28.
shout = "HELLO"
print(shout.isupper())

29.
mixed_case = "PyTHon" 
print(mixed_case.lower())

30.
print(mixed_case.upper())

31.
padded_text = " hello "
print(padded_text.lstrip())

32. 
print(padded_text.rstrip())

33. 
print(padded_text.strip())

34.
greetings = "Hello World!"
print(greetings.replace("World" , "Alice"))

35.
course_name = "Introduction to python"
print(course_name[0:12])
print(course_name[16:])

36.
quote = "To be or not to be, that is the question."
print(quote[0:18])
print(quote[20:])

37. 
phrase = "A Journey of a thousand miles begins with a single step"
print(phrase[50:55])
print(phrase[0:48])

38.
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(alphabet[0: :2])

39.
word = "tenet"
print(word[::-1])

40. 
sentence = "Learning Python is fun and rewarding!"
print(sentence[9 : 19])
print(sentence[0 : 10 : 2])
print(sentence[0: : 3])

41.
programming_language = "JavaScript"
print(programming_language[0:1:])
print(programming_language[9])

42.
data = "DataScience"
print(data[4:11:])

43. 
greetings = "good mornining!"
print(greetings[0::2])

44.
name = "Alexander"
first_three = name[:3]
last_three = name[-3:]
concatenate = first_three + last_three
print(concatenate)

age = 5
is_student = True 
name = "Awwal"
height = 4.65

template = "I am {},  It is {} that I am a student. I am {} years old, my height is {}"
print(template.format(name, is_student, age, height))
print(f"I am {name}, It is {is_student} that I am a student. I am {age} years old, my height is {height}")
print("I am " + name + ", It is that I am " + str(is_student) + ". I am " + str(age) + " years old, my height is " + str(height) )


temperature = 29.5
is_raining = False
no_of_cats = 7
name = "Zainab"
mood = "happy"
location = "Lagos"

template = "Hello, my name is {}, I live in {} and I have {} cats. It is {} that it is raining today, and the temperature is {}C. I am feeling {}"
print(template.format(name, location, no_of_cats, is_raining, temperature, mood,))
print(f"Hello, my name is {name}, I live in {location} and I have {no_of_cats} cats, It is {is_raining} raining today, and the temperature is {temperature}C. I am feeling {mood} ")
print("Hello, my name is " + name + ", I live in " + location + " and I have" + str(no_of_cats) + " cats, It is" + str(is_raining) + " raining today, and the temperature is" + str(temperature) + "C. I am feeling " + mood)

# Assignment 1

# 1. Format the following sentence using f-string, .format(), and concatenation:
"Welcome to Mars! This planet is 237 million years old. It is True that it is friendly to visitors. Gravity here is 3.721 m/s²."
planet = "Mars"
age = 237
is_friendly = True
gravity = 3.721
print("Welcome to {}! This planet is {} million years old. It is {} that it is friendly to visitors. Gravity here is {} m/s².".format(planet, age, is_friendly, gravity))
print(f"Welcome to {planet} This planet is {age} million years old. It is {is_friendly} that it is friendly to visitors. Gravity here is {gravity} m/s².")
print("Welcome to " + planet + "! This planet is " + str(age) + " million years old. It is " + str(is_friendly) + " that it is friendly to visitors. Gravity here is " + str(gravity) + " m/s².")



# 2. Format the following sentence using all three styles:
# "You are watching Inception. Your seat number is 45. It is false that this is a premium seat. The ticket costs $12.99."
movie = "Inception"
ticket_price = 12.99
seat_number = 45
is_premium = False
print("You are watching {}. Your seat number is {}. It is {} that this is a premium seat. The ticket costs ${}.".format(movie, seat_number, is_premium, ticket_price ))
print(f"You are watching {movie}. Your seat number is {seat_number}. It is {is_premium} that this is a premium seat. The ticket costs ${ticket_price}.")
print("You are watching "+ movie + ". Your seat number is " + str(seat_number) + ". It is " + str(is_premium) + " that this is a premium seat. The ticket costs $"+ str(ticket_price) + ".")


# 3. Compose this sentence using all three formatting styles:
"Sweet Crumbs is located in Downtown. We have 150 cakes today, each priced at $5.75 on average. It is True that we sell chocolate cakes."
bakery_name = "Sweet Crumbs"
num_cakes = 150
average_price = 5.75
has_chocolate = True
location = "Downtown"
print("{} is located in {}. We have {} cakes today, each priced at ${} on average. It is {} that we sell chocolate cakes.".format(bakery_name, location, num_cakes, average_price, has_chocolate))
print(f"{bakery_name} is located in {location}. We have {num_cakes} cakes today, each priced at ${average_price} on average. It is {has_chocolate} that we sell chocolate cakes.")
print( bakery_name + " is located in " + location + ". We have " + str(num_cakes) + " cakes today, each priced at $" + str(average_price) + " on average. It is " + str(has_chocolate) + " that we sell chocolate cakes.")


# 4. Create this sentence using all three formatting methods:
"Last night at Moonlight Arena, Aria Blaze performed 18 songs over 2.5 hours. It is True that the concert was live."
artist = "Aria Blaze"
duration = 2.5
num_songs = 18
was_live = True
venue = "Moonlight Arena"
print("Last night at {}, {} performed {} songs over {} hours. It is {} that the concert was live.".format(venue, artist, num_songs, duration, was_live))
print(f"Last night at {venue}, {artist} performed {num_songs} songs over {duration} hours. It is {was_live} that the concert was live.")
print("Last night at " + venue + ", " + artist + " performed " + str(num_songs) + " songs over " + str(duration) + " hours. It is " + str(was_live) + " that the concert was live.")


# 5. Format the following sentence using f-string, .format(), and concatenation:
"Meet Whiskers, a 2-year-old cat weighing 3.9 kg. It is True that Whiskers is vaccinated."
pet_name = "Whiskers"
pet_type = "cat"
weight = 3.9
age = 2
vaccinated = True
print("Meet {}, a {} years-old {} weighing {} kg. It is {} that {} is vaccinated.".format(pet_name, age, pet_type,  weight, vaccinated, pet_name))
print(f"Meet {pet_name}, a {age} years-old {pet_type} weighing {weight} kg. It is {vaccinated} that {pet_name} is vaccinated.")
print("Meet " + pet_name + ", a " + str(age) + " years-old " + pet_type + " weighing " + str(weight) + " kg. It is " + str(vaccinated) + " that " + pet_name + " is vaccinated." )

# unpacking
means_of_transport = ["car", "bus", "tricycle", "lorry", "boat", "ship", "plane", "broom"]
car, bus, tricycle, lorry, boat, ship, plane, broom = means_of_transport
print("bus", bus)
print("bus", bus)
print("tricycle", tricycle)
print("car", car)
print("lorry", lorry)
print("boat", boat)
print("ship", ship)
print("plane", plane)
print("broom", broom)



# Assignment
# 1. 
log_info = "george orwell ; 1984 ; 1949 ; ISN 978-0-452-28423-4 ; 328 ; 1999"
component = log_info.split(" ;")
author, book_title, year_published, isbn, no_of_pages, cost = component
author = author.title()
print(author)
print(component)
book_title = book_title.strip().title()
print(book_title)
year_published = year_published.strip().title()
isbn = isbn.replace("ISN", "ISBN").strip()
print(isbn)
no_of_pages = no_of_pages.strip()
# cost = cost.replace("1999", "#1999.00").strip()
print("{0:.2f}".format(float(cost)))
cost = "{0:.2f}".format(float(cost))
symbol = "#"
new_cost = symbol + cost
print(new_cost)


author = author
book_title = book_title
year_published = year_published
isbn = isbn
no_of_pages = no_of_pages
new_cost = new_cost

print("The book {} was written by {} and published in {}. It has {} pages and {} and costs {}.".format(book_title, author, year_published, no_of_pages, isbn, new_cost ))


2.
book_info_2 = "j.k. rowling ;  harry potter and the sorcerer's stone   ; 1997 ; ISN 978-0-590-35340-3 ; 309 ; 3499.997"
component = book_info_2.split(" ;")
print(component)
author1, book_title1, years, isbns, no_of_page, costs = component
author1 = author1.title()
book_title1 = book_title1.strip().title()
years = years.strip()
no_of_page = no_of_page.strip()
print(no_of_page)
isbns = isbns.replace("ISN", "ISBN")
costs = "{0:.2f}".format(float(costs))
symbol = "#"
new_costs = symbol + costs
print(new_costs)

author1 = author1
book_title1 = book_title1
years = years
isbns = isbns
no_of_page = no_of_page
costs = new_costs

print("The book {} was written by {} and published in {}. It has {} pages and {}  and costs {}.".format(book_title1, author1, years, no_of_page, isbns, new_costs ))

# 3
mary_info = "mary shelley ; frankenstein ; 1818 ; ISN 978-0-14-143947-1 ; 280 ; 2096.78"
component = mary_info.split(" ;")
print(component)
author_mary, title_mary, year_mary, isbn_mary, no_of_page_mary, cost_mary = component
author_mary = author_mary.title()
title_mary = title_mary.strip().title()
year_mary = year_mary.strip()
isbn_mary = isbn_mary.replace("ISN", "ISBN").strip()
no_of_page_mary = no_of_page_mary.strip()
cost_mary = "{0:.2f}".format(float(cost_mary))
symbol = "#"
new_cost_mary = symbol + cost_mary
print(new_cost_mary)

author_mary =  author_mary
title_mary =  title_mary
year_mary =  year_mary
isbn_mary =  isbn_mary
no_of_page_mary =  no_of_page_mary
cost_mary =  new_cost_mary


print("The book {} was written by {} and published in {}. It has {} pages and {} and costs {}.".format(title_mary, author_mary, year_mary, no_of_page_mary, isbn_mary, new_cost_mary))

# 4
hobbit_info = "j.r.r. tolkien ; the hobbit ; 1937 ; ISN 978-0-618-00221-3 ; 310 ; 2530.2134"
component = hobbit_info.split(" ;")
print(component)
author_hobbit, title_hobbit, year_hobbit, isbn_hobbit, page_hobbit, cost_hobbit = component 
author_hobbit = author_hobbit.title()
title_hobbit = title_hobbit.strip().title()
year_hobbit = year_hobbit.strip()
page_hobbit = page_hobbit.strip()
isbn_hobbit = isbn_hobbit.replace("ISN", "ISBN")
cost_hobbit = "{0:.2f}".format(float(cost_hobbit))
symbol = "#"
new_cost_hobbit = symbol + cost_hobbit
print(new_cost_hobbit)

print("The book {} was written by {} and published in {}. It has {} pages and {} and costs {}.".format(title_hobbit, author_hobbit, year_hobbit, page_hobbit, isbn_hobbit, new_cost_hobbit))

scott_info = "f. scott fitzgerald ;  the great gatsby ; 1925 ; ISN 978-0-7432-7356-5 ; 180 ; 2799"
component = scott_info.split(" ;")
scott_authur, scott_title, scott_year, scott_ibsn, scott_page_number, scott_cost = component
scott_title = scott_title.title().strip()
scott_authur = scott_authur.title()
scott_year = scott_year.strip()
scott_ibsn = scott_ibsn.replace("ISN", "ISBN")

scott_page_number = scott_page_number.strip()
scott_cost = "{0:.2f}".format(float(scott_cost))
symbol = "#"
new_scott_cost = symbol + scott_cost
print(new_scott_cost)

print("The book {} was written by {} and published in {}. It has {} pages and {} and costs {}.".format(scott_title, scott_authur, scott_year, scott_page_number, scott_ibsn, new_scott_cost))

# 5
mark_info = "markus zusak ; the book thief  ; 2005 ; ISN 978-0-375-83100-3 ; 552 ; 3199"
component = mark_info.split(" ;")
print(component)
mark_author, mark_title, mark_year, mark_isbn, mark_pages, mark_cost = component
mark_title = mark_title.title().strip()
mark_author = mark_author.title()
mark_year = mark_year.strip()
mark_isbn = mark_isbn.replace("ISN", "ISBN")
mark_pages = mark_pages.strip()
mark_cost = "{0:.2f}".format(float(mark_cost))
symbol = "#"
new_mark_cost = symbol + mark_cost
print(new_mark_cost)


print("The book {} was written by {} and published in {}. It has {} pages and {} and costs {}.".format(mark_title, mark_author, mark_year, mark_pages, mark_isbn, new_mark_cost))


# 6
jane_info = "jane austen ;  pride and prejudice  ; 1813 ; ISN 978-0-19-953556-9 ; 279 ; 1820.33434"
component = jane_info.split(" ;")
print(component)
jane_author, jane_title, jane_year, jane_pages, jane_ibsn, jane_cost = component
jane_author = jane_author.title().strip()
jane_title = jane_title.title().strip()
jane_year = jane_year.strip()
jane_pages = jane_pages.strip()
jane_ibsn = jane_ibsn.replace("ISN", "IBSN")
jane_cost = "{0:.2f}".format(float(jane_cost))
symbol = "#"
new_jane_cost = symbol + jane_cost

print("The book {} was written by {} and published in {}. It has {} pages and {} and costs {}.".format(jane_title, jane_author, jane_year, jane_pages, jane_ibsn, new_jane_cost))


# 7
leo_bookinfo = "leo tolstoy ;  war and peace ; 1869 ; ISN 978-0-14-044793-4 ; 1225 ; 4999"
component = leo_bookinfo.split(" ;")
print(component)
leo_authur, leo_title, leo_year, leo_isbn, leo_pages, leo_costs = component
leo_authur = leo_authur.title()
leo_title = leo_title.title().strip()
leo_year = leo_year.strip()
leo_isbn = leo_isbn.replace("ISN", "ISBN").strip()
leo_costs = "{0:.2f}".format(float(leo_costs))
symbol = "#"
new_leo_costs = symbol + leo_costs


print("The book {} was written by {} and published in {}. It has {} pages and {} and costs {}.".format(leo_title, leo_authur, leo_year, leo_pages, leo_isbn, new_leo_costs))

# 8
charles_bookinfo = "charles dickens ; a tale of two cities ; 1859 ; ISN 978-0-14-143960-0 ; 544 ; 2299"
component = charles_bookinfo.split(" ;")
print(component)
charles_authur, charles_title, charles_year, charles_isbn, charles_pages, charles_costs = component
charles_authur = charles_authur.title()
charles_title = charles_title.title().strip()
charles_isbn = charles_isbn.replace("ISN", "IBSN")
charles_costs = "{0:.2f}".format(float(charles_costs))
symbol = "#"
new_charles_costs = symbol + charles_costs

print("The book {} was written by {} and published in {}. It has {} pages and {} and costs {}.".format(charles_title, charles_authur, charles_year, charles_pages, charles_isbn, new_charles_costs))



# Section 2

# 1

# Assign values "Orange", "Banana", "Cherry" to multiple variables x, y and z in one line respectively.

x, y, z = "Orange", "Banana", "Cherry"
print(x, y, z)


# 2

# Assign the values 10, "John", and True to the variables age, name, and is_student in a 
# single line.

age, name, is_student = 10, "John", True
print(age, name, is_student)


# 3
# Swap the values of x and y, where x = 5 and y = 10, without using a temporary variable.

x = 5
y = 10
x, y = y, x
print(x, y)

# 4
# Create a list of numbers with values 1, 2, and 3. Unpack the list into separate 
# variables a, b, and c.

numbers = 1, 2, 3
a, b, c =  numbers
print(a, b, c)

# 5 
# Convert a string variable called height from “1.35” to a float.
height = "1.35"
print(float(height))

# 6 
# Predict the output of the following statements:
# 	a) bool("") = False
# b) bool(123) = True
# c) bool(["apple", "cherry", "banana"]) = True
# d) bool(False) = False
# e) bool(None) = False
# f) bool(0) = False
# g) bool("abc") = True
# h) bool(()) = False
# i) bool([]) = False
# j) bool({}) = False


# # 
# color = input("what is your favorite color? ")
# print(f"{color} is awesome")

# last_name = input("enter your last name? ")
# first_name = input("enter your first name? ")
# full_name = last_name + " " + first_name
# print(f"good morning, {full_name}!")

# birth_year = int(input("Enter your birth year: "))
# current_year = 2025
# age = current_year - birth_year
# print(f"You are {age} years old.")


# Assignment 2
#1
# Write a program that asks the user for their name and then greets them with their 
# name: Print a greeting message that includes the user's name in the format "Hello, {name}!".
# name = input("Enter your full name: ")
# print(f"Hello, {name}! How are you doing today?")


#2
# Ask the user for their birth year and calculate their age. Print the user's age in the 
# format “You are {age} years old.”.

# birth_year = input("What year were you born? ")
# age = datetime.now().year - int(birth_year)
# print(f"You are {age} years old.")


#3 
# Ask the user for their favourite color. Print a statement that includes the color in the format 
# “Your favorite color is {favourite_color}.”.

# favorite_color = input("What is your favorite color? ")
# print(f"Your favorite color is {favorite_color}.")



#4
# Ask the user to input some text and check if it is a palindrome. A palindrome is a word, phrase, or sequence 
# that reads the same backwards as forwards, e.g. `madam` or `nurses run` or `121`.
# Print a statement in the format “It is {is_palindrome} that {text} is a palindrome.”. `is_palindrome` is either `True` or `False`.

# text = input("Write some text: ")
# cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
# is_palindrome = cleaned_text == cleaned_text[::-1]

# print(f"It is {is_palindrome} that {text} is a palindrome.")

#5
# Create a program that asks the user to input a password and checks if it meets certain criteria (at least 8 characters and not more than 30 characters).
# Print a statement in the format “It is {is_valid} that the password fulfils the criteria.”. `is_valid` is either `True` or `False`.
# Bonus point if you can hide the password input from displaying on the screen as clear text.

password = input("Input your password? ")
is_valid = 8 <= len(password) <= 30

print(f"It is {is_valid} that the password fulfils the criteria.")


# 6
# Write a program that asks the user for their weight (in kilograms) and height (in meters) and calculates their Body Mass Index (BMI).
#  Calculate the BMI using the formula BMI = weight / (height ** 2). Round the BMI to 2 decimal places. Print a statement in the format “Your BMI is {BMI}”.

# weight = float(input("input your weight in (kilogram): "))
# height = float(input("Input your height in (meters): "))
# bmi = "{0:.2f}".format(weight / (height ** 2))
# print(f"Your BMI is {bmi}")
