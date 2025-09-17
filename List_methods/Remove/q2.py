# Question 2
# Start with this list
fruits = ["apple", "banana", "cherry", "banana", "mango"]


count = 0

count = 0
for idx, val in enumerate(fruits):
    if val == "banana":
        count += 1
        if count == 2:
            fruits.pop(idx)
            break

print(fruits)

# Remove only the second "banana" without using its index directly.
# Expected Output:
# ["apple", "banana", "cherry", "mango"]
