# Question 2 (append)

# Problem:
# Start with a list of strings. Append the reverse of the last element in the list.

words = ["python", "java"]


last_word = words[-1]
words.append(last_word[::-1])

print(words)


# Expected Output:

# ['python', 'java', 'avaj']
