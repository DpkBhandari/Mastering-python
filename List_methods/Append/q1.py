# Question 1 (append)

# Problem:
# You have a list of even numbers. Append the next even number automatically (no hardcoding).

nums = [2, 4, 6]

next_even_number = nums[-1] + 2
nums.append(next_even_number)
print(nums)


# Expected Output:

# [2, 4, 6, 8]
