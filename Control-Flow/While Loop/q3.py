# 🔹 While Loop Question 3 (Tricky)

# Problem Explanation:

# You have a number num = 9875.

# Using a while loop, repeatedly sum the digits of the number until you get a single-digit number.

# Print the final single-digit result.

# Starter Code:
num = 9875


while num > 9:
    total = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        total += digit
        temp //= 10
    num = total

print(num)
# Expected Output:
# 2
