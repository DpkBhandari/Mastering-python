# Question 2 (extend)

# Problem Explanation:
# You have a list of words. Another list contains words in uppercase. You need to extend the first list with only those uppercase words that are not already present in lowercase.

words = ["apple", "banana"]
upper_words = ["APPLE", "CHERRY"]
li = []

for i in upper_words:

    if i.lower() not in words:
        li.append(i)

words.extend(li)

print(words)
print(upper_words)


# Expected Output:

# ['apple', 'banana', 'CHERRY']


# (APPLE is skipped because "apple" already exists in lowercase. CHERRY is added.)
