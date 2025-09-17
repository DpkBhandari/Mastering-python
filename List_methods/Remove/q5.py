# Question 5
# Start with this list
nums = [5, 10, 15, 20, 25, 30]

i = 0
while i < len(nums):
    if nums[i] % 2 == 0:
        nums.remove(nums[i])
    else:
        i += 1

print(nums)

# Do not use list comprehension or filter.
# Expected Output:
# [5, 15, 25]
