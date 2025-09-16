# For Loop Question 3 (Trickier)

# Problem Explanation:

# You have a list of numbers:

# nums = [10, 25, 30, 45, 50, 60]


# Use a for loop to print numbers that are divisible by both 5 and 3, but instead of printing the number itself, print its half value.

nums = [10, 25, 30, 45, 50, 60]

for i in nums:
    if i % 5 == 0 and i % 3 == 0:
        print(i / 2)


# Expected Output:

# 15
# 22.5
# 30
