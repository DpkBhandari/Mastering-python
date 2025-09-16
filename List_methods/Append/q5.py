# Question 5 (append)

# Problem:
# You have a list of numbers. Append the first number that is missing in the sequence.

nums = [1, 2, 3, 5, 6]


for j in range(
    1, max(nums) - 1
):  # this will find the largest num in list loop goes till that nums- 1
    if not j in nums:
        nums.append(j)
        break


print(nums)


# Expected Output:

# [1, 2, 3, 5, 6, 4]
