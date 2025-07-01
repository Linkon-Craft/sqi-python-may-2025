book_info = "harper lee ; to kill a mockingbird ; 1960 ; ISN 978-0-06-112008-4 ; 324 ; 2999.4789"
components = book_info.split(" ; ")
author, book_title, year_published, isbn, no_of_pages, cost = components
author = author.title()
print(author)
book_title = book_title.strip().title()
print(book_title)

print(year_published)
print(isbn)
print(no_of_pages)
print(cost)



# age = 5
# is_student = True
# name = "Awwal"
# height = 4.65
# print("I am {2}. It is {0} that I am a student. I am {1} years old, my height is {3}m".format(is_student, age, name, height))


radius = "45.2345"
# print("{0:.2f}".format(radius))
# print("{1:.2f}".format(radius, 32.789))
# print("{0:.2f}".format(radius, 32.789))
print(type("{0:.2f}".format(radius, 32.789)))


radius = 45.2762
print(round(radius))
print(type(round(radius)))

