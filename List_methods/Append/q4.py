# Question 4 (append)

# Problem:
# You have a list of sublists. Append a new sublist that contains the length of each existing sublist.

lists = [[1, 2], [3, 4, 5], [6]]
length = []
for i in lists:
    length.append(len(i))


lists.append(length)

print(lists)


# Expected Output:

# [[1, 2], [3, 4, 5], [6], [2, 3, 1]]
