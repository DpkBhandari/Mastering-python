# Question 1 (extend)

# Problem Explanation:
# You have two lists:

# a = [1, 2, 3]
# b = [4, 5]


# If you do a.append(b) → result will be [1, 2, 3, [4, 5]]. (b is added as one single element.)
# But we want [1, 2, 3, 4, 5]. That means we should use extend.

# Task:
# Extend list a with elements of list b.

a = [1, 2, 3]
b = [4, 5]

a.extend(b)


print(a)


# Expected Output:

# [1, 2, 3, 4, 5]
