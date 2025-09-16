# If-Else Question 5 (Tricky)

# Problem Explanation:

# You have a number num.

# Check the following using if-else:

# If num is negative and odd → print "Negative Odd"

# Else if num is negative and even → print "Negative Even"

# Else if num is positive and odd → print "Positive Odd"

# Else → print "Positive Even"

num = -7
if num < 0 and not num % 2 == 0:
    print("Negative Odd")

elif num < 0 and num % 2 == 0:
    print("Negative Even")
elif num > 0 and not num % 2 == 0:
    print("Positive Odd")

else:
    print("Positive Even")


# Expected Output:

# Negative Odd
