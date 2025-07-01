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
# Stage 1
confirmed_guests = ["Alice", "Charlie", "Eve", "Bob", "Frank", "Grace", "David", "Hannah", "Liam", "Mia"]
waitlist = []
print("\n\nStage 1")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)

# Stage 2
waitlist.extend(["Ken", "Jack", "Ivy"])
print("\n\nStage 2")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)


# Stage 3
waitlist.append("Noah")
waitlist.append("Oliver")
print("\n\nStage 3")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)

# # stage 4
# Alice has a family emergency and won’t be able to attend the wedding, She cancels her attendance.
# Remove Alice from the confirmed guest list and add the first person from the waitlist to the confirmed list. 
confirmed_guests.remove("Alice")
confirmed_guests.append(waitlist[0])
waitlist.remove("Ken")
print("\n\nStage 4")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)


# Stage 5
# Charlie is the godfather of the groom and he is the one funding the wedding. Therefore he is a VIP guest and
# the couple has asked you to make sure he is on the guestlist. Check whether or not Charlie is on the guestlist.
print("Charlie" in confirmed_guests)
print("\n\nStage 5")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)



# stage 6 
# David and Eve have decided they no longer want to attend the wedding and therefore cancel their attendance. 
# Remove them from the confirmed_guests list. 
confirmed_guests.remove("Eve")
confirmed_guests.remove("David")
print("\n\nStage 6")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)


# Stage 7
# Move the first 2 people on the waitlist into the guestlist to fill up the newly freed slots.
print(waitlist)
confirmed_guests.append("Jack")
confirmed_guests.append("Ivy")
waitlist.remove("Jack")
waitlist.remove( "Ivy")
print("\n\nStage 7")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)

# Stage 8
# Oliver just realized the day of the wedding is the same day he has to take his pet to see the vet and he 
# cancels his attendance. Remove him from the waitlist.
print(waitlist)
waitlist.remove("Oliver")
print("\n\nStage 8")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)


# State 9
# The event planner has asked you for the names of the last 3 guests on the guest list because she needs 
# to make additional arrangements for them. Get her this information.
print(confirmed_guests)
print("Last 3 names: ", confirmed_guests[7:])
print("\n\nStage 9")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)

# Stage 10
# The bride and groom have decided that they want to allow room for 5 more people to attend their wedding. Move 
# waitlisted guest (Noah) into the confirmed_guests list.
confirmed_guests.append("Noah")
waitlist.remove("Noah")
print("\n\nStage 10")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)


# Stage 11
# The event planner wants a report on the number of people
# who will be attending the wedding. Give her this information.
print("No of People: ", len(confirmed_guests))
print("\n\nStage 11")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)


# Stage 12
# The event planner has also requested that you give her a list of all the names of the confirmed_guests. 
# The guests would be seated alphabetically at the venue and so she wants the names in alphabetical order.
confirmed_guests.sort()
print("\n\nStage 12")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)


# Stage 13
# A new guest called Collins who is the son of Grace and Noah would be attending on their behalf, Replace Grace 
# and Noah on the confirmed_guests list with Collins. Make sure you re-sort the list.
confirmed_guests.remove("Grace" and "Noah")
confirmed_guests.append("Collins")
confirmed_guests.sort()
print("\n\nStage 13")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)


# Stage 14
# The caterer has also requested for the confirmed_guests list so she can provide the guests with customized bags 
# containing their food with their names on it. Give her a copy of the confirmed_guests list titled guests_list_for_caterer`.

import copy
confirmed_guests_for_Caterer = copy.copy(confirmed_guests)
print("\n\nStage 14")
print("Confirmed guests: ", confirmed_guests)
print("Confirmed guests for caterer: ", confirmed_guests_for_Caterer)
print("Waitlist: ", waitlist)

# Stage 15
# The deadline for accepting the invitations sent has now passed. There is no more need for the waitlist. Clear the 
# waitlist.
del waitlist
print("\n\nStage 15")
print("Confirmed guests: ", confirmed_guests)
print("Confirmed guests for caterer: ", confirmed_guests_for_Caterer)

