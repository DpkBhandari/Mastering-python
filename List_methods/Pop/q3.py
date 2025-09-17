# Question 3
# Start with this list
nums = [100, 200, 300, 400, 500]

elements = []

while len(nums) > 0:
    ele = nums.pop()
    elements.append(ele)
print("Popped elements in order:", *elements)
# Use pop() to remove elements one by one from the **end** of the list
# and print them until the list becomes empty.
# Expected Output:
# Popped elements in order: 500 400 300 200 100
