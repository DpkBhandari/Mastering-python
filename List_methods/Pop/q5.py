# Question 5
# Start with this list
import math

letters = ["p", "q", "r", "s", "t"]


length = len(letters)
length = math.floor(length / 2)
print(length)
ele = letters.pop(length)


print(f"Updated list: {letters}")
print(f"Popped element: {ele}")

# Pop the **middle element** dynamically (without hardcoding the index)
# Print the updated list and the popped element
# Expected Output:
# Updated list: ['p', 'q', 's', 't']
# Popped element: 'r'
