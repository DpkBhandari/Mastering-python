# 🔹 While Loop Question 1 (Tricky)

# Problem Explanation:
# You have a number num = 12345.
# Using a while loop:

# Reverse the number.

# Print the reversed number.

# Starter Code:
num = 12345
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

print(rev)


# Expected Output:
# 54321
