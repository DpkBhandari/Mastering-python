# If-Else Question 3 (Tricky)

# Problem Explanation:

# You have a number num.

# Check the following using if-else:

# If num is prime → print "Prime"

# Else if num is even → print "Even"

# Else → print "Odd"

num = 17
isPrime = True

print(int(num**0.5))
if num < 2:
    isPrime = False
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            isPrime = False
            break

if isPrime:
    print("Prime")

elif num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Expected Output:

# Prime
