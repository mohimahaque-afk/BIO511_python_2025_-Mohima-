# Create a script (.py file) where you save one value of each data type to its own variable.
# Afterwards, print all the variables and their type using print() and type()
# Data types to include: integer, floating point, string, boolean, nonetype,
# list, dictionary, tuple, set, range 
print("Part 1: Variables and types")
whole_number = 10
decimal_number = 3.14
text = "Hello, World!"
reality_check = True
nothing = None
fruits = ["apple", "banana", "cherry"]
person = {"name": "Alice", "age": 30}
coordinates = (10.0, 20.0)
unique_numbers = {1, 2, 3}
number_range = range(35, 100)

variables = [whole_number, decimal_number, text, reality_check, nothing, fruits, person, coordinates, unique_numbers, number_range]
for var in variables:
    print(f"Value: {var}, Type: {type(var)}")

# A) Simple check (If/else clause)
# Pick a STRING you created. 
# If it is empty print "empty", else print "non-empty".
# (Hint: len(...) )
# Your code below
text = "Hello, World!"
if len(text)== 0:
    print(f"The string is empty")
else:
    print(f"The string is not empty.")

print("B: Multi-way - if/elif/else clause")
# B) Multi-way (If/elif/else clause)

# Pick an INTEGER you created.
# Print exactly one of: "negative", "zero", "positive".
# (Hint: compare to 0)

# Your code below
if whole_number == 0:
    print(f"The integer is zero.")
elif whole_number > 0:
    print(f"The integer is positive.")
else:
    print(f"The integer is negative.")
# C) Type gate + nested classification (Nested If/elif/else)
print("\n")
# Pick a SEQUENCE you created (list OR tuple OR range).
# If the type of the variable matches your choice, check:
#   - if length == 0 print "empty"
#   - elif length == 1 print "single item"
#   - else print "multiple items"
# Else print "wrong type for this task".
# (Hint: type(x) is list/tuple/range; len(...) )

# Your code below

if type(fruits) == list:
    pass
    if len(fruits) == 0:
        print(f"The input is empty.")
    elif len(fruits) == 1:
        print(f"The input has a single item.")
    else:
        print(f"The input has multiple items.")
else:
    print(f"The input is wrong type for the task.")
    
    