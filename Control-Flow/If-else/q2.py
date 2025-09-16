# If-Else Question 2 (Tricky)

# Problem Explanation:

# You have an integer num.

# Check the following using if-else:

# If num is negative → print "Negative"

# Else if num is even and greater than 50 → print "Large Even"

# Else if num is even but ≤ 50 → print "Small Even"

# Else → print "Odd"

num = 72

if num < 0:
    print("Negative")
elif num % 2 == 0 and num > 50:
    print("Large Even")
elif num % 2 == 0 and num <= 50:
    print("Small Even")

else:
    print("Odd")


# Expected Output:

# Large Even
