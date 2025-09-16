# ChatGPT said:
# 🔹 While Loop Question 4 (Tricky)

# Problem Explanation:

# You have a number num = 12321.

# Using a while loop, check if the number is a palindrome (reads the same forwards and backwards).

# Print "Palindrome" if true, else "Not Palindrome".

# Starter Code:
num = 12321
rev = 0
temp = num

while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10

if rev == num:
    print("Palindrome")
else:
    print("Not an Palindrome")

# Expected Output:
# Palindrome
