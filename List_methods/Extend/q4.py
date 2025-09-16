# Question 4 (extend)

# Problem Explanation:

# You have a list of lists:

# matrix = [[1, 2], [3, 4]]


# Your task is to flatten all the inner lists and create a single list containing all elements.

# Input: [[1, 2], [3, 4]]

# Output: [1, 2, 3, 4]

# Starter Code:

matrix = [[1, 2], [3, 4]]
li = []

for i in matrix:
    for j in i:
        print(j)
        li.append(j)

matrix.clear()
matrix.extend(li)

print(matrix)


# Expected Output:

# [1, 2, 3, 4]