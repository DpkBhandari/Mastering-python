# For Loop Question 5 (Tricky – Strings + Loop)

# Problem Explanation:

# You have a list of strings:

# words = ["python", "java", "cpp", "ruby"]


# Task:

# Use a for loop to print only those words where:

# The word length is greater than 3.

# The word contains the letter 'a'.

# For the words that satisfy these conditions, also print the word in uppercase.

# Starter Code:
words = ["python", "java", "cpp", "ruby"]

for i in words:
    if len(i) > 3 and "a" in i:
        print(i.upper())

# Expected Output:
# JAVA
