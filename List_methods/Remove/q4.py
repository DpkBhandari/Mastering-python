# Question 4
# Start with this list
data = ["x", "y", "z", "y", "w"]

count = 0

for i in data:
    if i == "y":
        count += 1
        if count > 1:
            data.remove(i)


print(data)


# Remove "y" only if it appears more than once.
# (If "y" appears once, leave the list unchanged)

# Expected Output:
# ["x", "z", "y", "w"]
