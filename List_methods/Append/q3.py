# Question 3 (append)

# Problem:
# Create a list of numbers. Append the sum of only the odd numbers present in the list.

nums = [5, 10, 15, 20]
sum = 0
for i in nums:
    if not i % 2 == 0:
        sum += i


nums.append(sum)

print(nums)


# Expected Output:

# [5, 10, 15, 20, 20]
