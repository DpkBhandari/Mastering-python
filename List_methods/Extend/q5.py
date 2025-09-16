# Question 5 (extend)

# Problem Explanation:

# You have a list of words:

# words = ["hello", "world"]


# You are also given a list of strings:

# extra_words = ["hi there", "good morning"]


# Task: Split each string in extra_words into individual words and extend them into the words list.

# Example: "hi there" → "hi", "there" will be added.

# Starter Code:

words = ["hello", "world"]
extra_words = ["hi there", "good morning"]

li = []

for i in extra_words:
    for j in i.split():
        li.append(j)

words.extend(li)

print(words)


# Expected Output:

# ['hello', 'world', 'hi', 'there', 'good', 'morning']
