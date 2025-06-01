'''
# 1. Introduction to Collections
# Problem with storing multiple values using separate variables:
# Example: roll_1 = value_1, roll_2 = value_2, ..., roll_n = value_n
# Solution: Use container data types like List, Tuple, Set, etc.

# 2. Introduction to Lists
numbers = [1, 2, 3, 4]
list_1 = [1, 2, 3, 4, 5, 6]
list_2 = ['a', 'b', 'c', 'd']
list_3 = ['apple', 'orange', 2000, 69.6]

# 3. Accessing Values in a List
values = [15, 20, 96, 32, 17]
print("Indexing:")
print(values[0])  # 15
print(values[4])  # 17

print("Slicing:")
print(values[0:3])  # [15, 20, 96]
print(values[2:5])  # [96, 32, 17]

# 4. Appending Values to a List
values.append(60)
print("After appending 60:", values)

# 5. Updating a Value in a List
values[2] = 60
print("After updating index 2 to 60:", values)

# 6. Deleting a Value from a List
# Using remove() method (removes by value)
values = [15, 20, 96, 32, 17]
values.remove(20)
print("After removing 20:", values)

# Using del keyword (removes by index)
values = [15, 20, 96, 32, 17]
del values[1]
print("After deleting index 1:", values)

# Practice Exercise 1
list1 = ['ph', 'ch', 1997, 2000, 2000, 2009]
list1[2] = 2001
list1.remove(2000)
list1.append(2015)
print("Exercise 1 Output:", list1[2:])  # Expected: [2001, 2000, 2009, 2015]

# 7. Multi-dimensional Lists (Matrix)
data = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
print("Accessing 2D list:", data[1][1])  # 2

# Update
data[1][1] = 25
print("After update:", data)

# Append to internal list
data[1].append(2)
print("After appending 2 to row 2:", data)

# 8. List Operations

# Length
print("Length of [1,2,3]:", len([1, 2, 3]))

# Concatenation
a = [1, 2, 3]
b = [4, 5, 6]
print("Concatenation of a and b:", a + b)

# Repetition
print("Repetition:", ['Hi'] * 4)

# Membership
print("Is 3 in [1,2,3]?", 3 in [1, 2, 3])  # True
print("Is 5 in [1,2,3]?", 5 in [1, 2, 3])  # False

# Iteration
print("Iterating through list:")
for x in [1, 2, 3]:
    print(x)

'''