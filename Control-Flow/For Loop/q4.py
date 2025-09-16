# For Loop Question 4 (Tricky – Nested Loop)

# Problem Explanation:

# You have a list of lists (matrix):

# matrix = [[2, 5, 8], [3, 6, 9], [4, 7, 10]]


# Task:

# Use a nested for loop.

# From each sublist, print only the numbers that are even and greater than 5.

# Starter Code:
matrix = [[2, 5, 8], [3, 6, 9], [4, 7, 10]]

for i in matrix:
    for j in i:
        if j % 2 == 0 and j > 5:
            print(j)

# Expected Output:
# 8
# 6
# 10
