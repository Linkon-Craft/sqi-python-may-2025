my_info = {"first_name": "Lekan", "is_male": "True", "age": "26", "complexion": "dark"}
print(my_info)
my_info["height"] = 5.7
print(my_info)
del my_info["age"]
my_info["first_name"] = "Usman"
print(my_info)
print("weight" in my_info)
print(False in my_info)
print(len(my_info))
print(my_info.keys())
print(list(my_info.values()))
print(my_info.items)
my_info.clear()
print(my_info)
del my_info



