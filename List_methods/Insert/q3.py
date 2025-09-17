# Question 3
# Start with this list
import math

nums = [1, 2, 3, 4, 5]


length = len(nums)
length = math.ceil(length / 2)
nums.insert(length, 100)

print(nums)


# Insert 100 exactly in the middle of the list.
# (Your code should work even if the list length changes)

# Expected Output:
# [1, 2, 3, 100, 4, 5]
