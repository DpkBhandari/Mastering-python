# If-Else Question 4 (Tricky)

# Problem Explanation:

# You have an integer num.

# Check the following using if-else:

# If num is a multiple of 4 and 6 → print "Multiple of 4 & 6"

# Else if num is a multiple of 4 only → print "Multiple of 4"

# Else if num is a multiple of 6 only → print "Multiple of 6"

# Else → print "Not multiple of 4 or 6"

num = 24


if num % 4 == 0 and num % 6 == 0:
    print("Multiple of 4 & 6")
elif num % 4 == 0:
    print("Multiple of 4")
elif num % 6 == 0:
    print("Multiple of 6")
else:
    print("Not multiple of 4 or 6")


# Expected Output:

# Multiple of 4 & 6
