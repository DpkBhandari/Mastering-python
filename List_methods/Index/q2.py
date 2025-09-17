# Question 2 (tricky)
# Start with this list
nums = [10, 20, 30, 20, 40, 20]

count = 0
for idx, val in enumerate(nums):
    if val == 20:
        count += 1
        if count == 2:
            print(idx)
            break

# Find the index of the **second occurrence** of 20
# Expected Output: 3
