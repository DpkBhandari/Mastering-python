# 🔹 While Loop Question 2 (Tricky)
# Problem Explanation:

# You have a number num = 987654.

# Using a while loop, print only the even digits in reverse order.

# Starter Code:
num = 987654
rev = 0
while num > 0:
    digit = num % 10
    if digit % 2 == 0:
        print(digit)
    num//=10    

# Expected Output:
# 4
# 6
# 8
