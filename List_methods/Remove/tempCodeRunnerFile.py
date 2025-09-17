# Question 2
# Start with this list
fruits = ["apple", "banana", "cherry", "banana", "mango"]


count = 0

for i in fruits:
    if i == "banana":
        count += 1
        if count == 2:
            fruits.remove(i)
            break


print(fruits)

# Remove only the second "banana" without using its index directly.
# Expected Output:
# ["apple", "banana", "cherry", "mango"]
