# Question 2
# Start with this list
chars = ["a", "b", "d", "e"]

idx = chars.index("d")
chars.insert(idx, "c")
print(chars)

# Insert "c" without using the index number 2 directly.
# (Hint: Use list methods like index() to find where "d" is)

# Expected Output:
# ["a", "b", "c", "d", "e"]
