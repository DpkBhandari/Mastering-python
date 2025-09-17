# Question 5 (tricky)
# Start with this list
data = ["x", "y", "z", "y", "x"]

idx = len(data) - 1 - data[::-1].index("x")
print(idx)


# Find the index of the **last "x"** using only `index()` (hint: use negative indexing logic)
# Expected Output: 4
