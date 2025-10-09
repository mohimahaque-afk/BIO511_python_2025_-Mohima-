"Functions: Defining a function - 3. example"

def add_two_numbers(num_one, num_two):
    number_to_return = num_one + num_two
    return number_to_return

my_added_numbers = add_two_numbers(1, 1)

print("These are the added numbers{my_added_numbers}.") # will print 2

"4. Exercises"
# Provided inputs (use these)
nums = [3, -1, 7, 2, 9, 0, 4]
limit = 4
text = "Room 101: bring 2 apples & 1 banana."

# Globals to observe name masking (same-name local variables hides the global variable so use different variable names inside the function). Do not rename these.
count = 999
summary = "unset"
result = "unset"

print("4.1 - Count the number of items above limit")

"""
Count-above  (uses nums, limit, count)
Goal: make a small function called whatever you want and then call(run) it.

a) Define a function named count_above that takes two arguments: seq and lim.
b) Inside the function, create a LOCAL variable named count starting at 0.

c) Loop through seq; for each number strictly greater than lim, increase count by 1.

d) Return count.

e) Outside the function:
   - Print the GLOBAL count.
   - Call count_above(nums, limit) and print the returned number.
   - Print the GLOBAL count again (notice the global didn’t change).

Your code below
"""

def count_above(seq, lim):
    lopande = 0
    for i in seq:
        # print(i)
        if i > lim:
            lopande +=1
            # print(lopande)
            # import pdb; pdb.set_trace()
    return lopande

print(f"There are {count_above(nums, limit)} numbers bigger than {limit} in {nums}.")

## there are two numbers bigger than the limit: 4, therefore, the output is two.
print("4.2 - Text summary")
"""Text summary  (uses text, summary)
Goal: classify characters with an if/elif/else chain and return a clear result.

a) Define a function named summarize_text that takes one argument: s.

b) Inside the function, create a LOCAL variable named summary that holds a result dictionary
   with exactly these keys: "digits", "letters", "other" — each starting at 0.

c) Loop through each character in s:
      - if the character is a digit, increase "digits"
      - elif the character is a letter, increase "letters"
      - else increase "other"

d) Return the summary dictionary.

e) Outside the function:
   - Print the GLOBAL summary.
   - Call summarize_text(text) and print the returned dictionary.
   - Print the GLOBAL summary again.

text = "Room 101: bring 2 apples & 1 banana."
summary = "unset"

Your code below
"""
text = "Room 101: bring 2 apples & 1 banana."
summary = "unset"

def summarize_text(s):
    summary = {"digits": 0 , "letters": 0, "other": 0}
    for char in s:
        if char.isdigit():
            summary["digits"] +=1
        elif char.isalpha(): # check string has at least one letter
            summary["letters"] +=1
        else:
            summary["other"] +=1
    return summary

# e) Outside the function:
#    - Print the GLOBAL summary.
#    - Call summarize_text(text) and print the returned dictionary.
#    - Print the GLOBAL summary again.            

print(summary)
print(summarize_text(text))
print(summary)

print("\n", "4.3 - Nested Decisions based on a mode string.", "\n")


#C) Aggregate with mode  (uses nums, limit, result)
# Goal: nested decisions based on a mode string. Return one final value.

# a) Define a function named aggregate that takes three arguments: seq, mode, threshold.

# b) Inside the function, create a LOCAL variable named result.
#    Initialize it based on mode:
#       - if mode is "sum": start at 0
#       - if mode is "count": start at 0
#       - if mode is "max": start at None (meaning “no qualifying value yet”)

# c) Loop through each number n in seq:
#       - First, ignore n if it is negative (skip it).
#       - If n is at least threshold, then:
#           * if mode is "sum": add n to result
#           * elif mode is "count": increase result by 1
#           * else (treat any other mode as "max"):
#                 if result is None or n is greater than result, update result to n

# d) Return the result.

# e) Outside the function:
#    - Print the GLOBAL result.
#    - Call and print each of these:
#         aggregate(nums, "sum", limit)
#         aggregate(nums, "count", limit)
#         aggregate(nums, "max", limit)
#    - Print the GLOBAL result again.

# Your Code below
nums = [3, -1, 7, 2, 9, 0, 4]
limit = 4
result = "unset"
def aggregate(seq, mode, threshold):
    
    if mode is "sum" or "count":
        result = 0
    elif mode == "max":
        result = None
    
    for n in seq:
        if n < 0:
            continue
        if n >= threshold:
            if mode == "sum":
                result += n
            elif mode == "count":
                result += 1
            else:
                if result is None or n > result:
                    result = n
    return result

print(result)
print(f"Sum: {aggregate(nums, "sum", limit)}")    
print(f"Count: {aggregate(nums, "count", limit)}")
print(f"Max: {aggregate(nums, "max", limit)}")
print(result)
            
        
