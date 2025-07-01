# from collections import Counter

# with open("simple_data.csv", "r") as f:
#     contents = f.read()
#     # contents = f.readlines()


# rows = contents.strip().split("\n")
# headers = rows[0]
# rows = rows[1:]
# names = []
# ages = []
# sum_of_ages = 0
# names_and_ages = []
# for row in rows:
#     row_id, name, age, country = row.split(",")
#     names.append(name)
#     age = int(age)
#     ages.append(age)
#     names_and_ages.append({"name": name, "age": age})

# names.sort()
# sum_of_ages = sum(ages)
# print(f"Avg age: {sum_of_ages/len(rows)}")


# age_occurrences = dict(Counter(ages))


# most_occurring_age = list(age_occurrences.keys())[0]
# no_of_occurences_most_occuring_age = list(age_occurrences.values())[0]
# for age, occurence in age_occurrences.items():
#     if occurence > no_of_occurences_most_occuring_age:
#         no_of_occurences_most_occuring_age = occurence
#         most_occurring_age = age

# print("Most occuring age: ", most_occurring_age)

# most_occurring_age_people = []
# for name_age in names_and_ages:
#     name, age = name_age["name"], name_age["age"]
#     if age == most_occurring_age:
#         most_occurring_age_people.append(name)


# print(f"People with the most occuring age: {most_occurring_age_people}")


# from datetime import datetime
# with open("created-with-python.md", "a") as f:
#     f.write(f"""This file was created by Python on {datetime.now()}.
# We are learning how to read from and write to files using Python.""")



# Output
# Line 1: Hello
# Line 2: I am at SQI today
# Line 3: I am a student
# Line 4: I love Python
# Line 5: Python is amazing

# with open("new_file.txt", "r") as f:
#     lines = f.readlines()
#     for idx, line in enumerate(lines, start=1):
#         print(f"Line {idx}: {line.strip()}")


# MANUAL FILE HANDLING
# f = open("new_file.txt", "w")
# f.write("This is new content")
# f.close()

with open("new_text.txt", "w") as f:
    f.write("""
Alice,30
Fiona,28
Jasmine,31
George,33
Bob,25
Ella,22
Hannah,27
Daniel,40
Isaac,29
Charlie,35
""")
    
with open("new_text.text", "r") as f:
    content = f.readlines()
    print(content)


