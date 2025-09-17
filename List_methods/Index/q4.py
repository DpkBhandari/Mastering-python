# Question 4 (tricky)
# Start with this list
nums = [5, 10, 15, 20, 25, 30, 15]

# Find the index of 15 **between index 2 and 5** (inclusive of start, exclusive of end)
# Expected Output: 2


idx = nums.index(15, 2, 5)
print(idx)
