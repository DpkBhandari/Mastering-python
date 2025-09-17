# Question 2
# Start with this list
data = [[1, 2], [3, 4], [5, 6]]

for i in data:
    i.clear()

print(data)

# Clear only the **inner lists** without deleting the outer list structure.
# Expected Output: [[], [], []]
