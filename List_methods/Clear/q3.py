# Question 3 (tricky)
# Start with this list
nums = [1, 2, 3, 4, 5]

nums_copy = nums.copy()
nums.clear()

print(f"nums : {nums}")
print(f"nums_copy : {nums_copy}")
# Copy nums into nums_copy, then clear nums.
# Print both lists to show that nums_copy still retains its values.
# Expected Output:
# nums: []
# nums_copy: [1, 2, 3, 4, 5]
