# Question 3 (extend)

# Problem Explanation:
# You have a list of numbers. You want to extend the list with all numbers from another list that are divisible by 3, keeping the original list unchanged for other numbers.

nums = [2, 5, 7]
extras = [3, 6, 9, 10]  # list wohi numbers ko add karna hai jo divisible by 3 ho
li = []  # empyt list to store the values of list which are divisible by 3
for i in extras:  # extraing all which are divisible by 3 and storing it in new li
    if i % 3 == 0:
        li.append(i)

nums.extend(li)  # extending the new list to nums

print(nums)  # Printing The Value Of nums


# Expected Output:

# [2, 5, 7, 3, 6, 9]


# (10 is ignored because it’s not divisible by 3.)
