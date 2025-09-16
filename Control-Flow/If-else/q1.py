# If-Else Question 1 (Tricky)

# Problem Explanation:

# You have a number num.

# If num is divisible by both 2 and 3 → print "Divisible by 2 & 3"

# Else if num is divisible by 2 only → print "Divisible by 2"

# Else if num is divisible by 3 only → print "Divisible by 3"

# Else → print "Not divisible by 2 or 3"

num = 12


if num % 2 == 0 and num % 3 == 0:
    print("Divisible by 2 & 3")
elif num % 2 == 0:
    print("Divisible by 2")
elif num % 3 == 0:
    print("Divisible by 3")
else:
    print("Not divisible by 2 or 3")

# Expected Output:

# Divisible by 2 & 3
