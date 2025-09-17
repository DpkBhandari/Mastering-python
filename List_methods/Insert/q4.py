# Question 4
# Start with this list
fruits = ["apple", "banana", "cherry"]

length = len(fruits) - 1

fruits.insert(length, "mango")
print(fruits)

# Insert "mango" at the second last position,
# no matter how long the list is.

# Expected Output:
# ["apple", "banana", "mango", "cherry"]
