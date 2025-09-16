# For Loop Question 2 (Tricky)

# Problem Explanation:

# You have a list of strings:

# words = ["apple", "banana", "cherry", "date"]


# Use a for loop to print only the words that contain the letter 'a' but not 'e'.

words = ["apple", "banana", "cherry", "date"]


for i in words:
    if "a" in i and not "e" in i:
        print(i)

# Expected Output:

# banana
