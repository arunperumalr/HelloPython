# ********************** SET **********************
print("********************** SET **********************")
print("A set is an unordered collection of unique elements.")
print()

#Creating a Set
my_set = {1, 2, 3}
print("my_set: ",my_set) # OUTPUT: my_set:  {1, 2, 3}
print()

#Empty Set : Use set() because {} creates a dictionary.

empty = set()
print(type(empty)) # OUTPUT: <class 'set'>
print()

#Adding Elements
s = {1, 2, 3}
s.add(4)
print(s) # OUTPUT: {1, 2, 3, 4}
print()

# update() — Add Multiple Elements
s = {1, 2}
s.update([3, 4, 5])
print(s) # OUTPUT: {1, 2, 3, 4, 5}
print()

# Removing Elements : remove() - Throws error if item not found.
s = {1, 2, 3}
s.remove(2)
print(s) # OUTPUT: {1, 3}
print()

# Removing Elements : discard() - Does NOT throw error.
s = {1, 2, 3}
s.discard(5)
print(s) # OUTPUT: {1, 2, 3}
print()

# Removing Elements : pop() - Removes a random element.

s = {10, 20, 30}
removed = s.pop()
print("Removed Element: ",removed) # Removed Element:  10
print("After Removal: ",s) # After Removal:  {20, 30}
print()

# Removing Elements : clear() - Removes Everything.
s = {1, 2, 3}
s.clear()
print("After Clear: ",s) # After Clear:  set()
print()

#Union : Combines all unique elements.
a = {1, 2, 3}
b = {3, 4, 5}
print("Union: ",a | b) # Union:  {1, 2, 3, 4, 5}
print("Union: ",a.union(b)) # Union:  {1, 2, 3, 4, 5}
print()

#Intersection : Common elements only.
a = {1, 2, 3}
b = {2, 3, 4}
print("Intersection: ",a & b) # Intersection:  {1, 2, 3, 4, 5}
print("Intersection: ",a.intersection(b)) # Intersection:  {1, 2, 3, 4, 5}
print()

#Difference : Elements present in first set only.
a = {1, 2, 3}
b = {2, 3, 4}
print("Difference: ",a - b) # Difference:  {1}
print("Difference: ",a.difference(b)) # Difference:  {1}
print()

#Symmetric Difference : Elements not common in both sets.
a = {1, 2, 3}
b = {3, 4, 5}
print("Symmetric Difference: ",a ^ b)
print("Symmetric Difference: ",a.symmetric_difference(b))
print()

# Membership Test
s = {10, 20, 30}
print(20 in s) # True
print(100 not in s) # True
print()

#Iterating Through Set
colors = {"red", "green", "blue"}

for color in colors:
    print(color)
# red green blue
print()

# Length of Set
s = {1, 2, 3, 4}
print(len(s)) # 4
print()

#Copying a Set
s1 = {1, 2, 3}
s2 = s1.copy()
print(s2) # {1, 2, 3}
print()

# Set Comparison
a = {1, 2}
b = {1, 2, 3}
print("SUBSET: ",a.issubset(b)) # True
print("SUPERSET: ",b.issuperset(a)) # True
print()

# Disjoint Sets
a = {1, 2}
b = {3, 4}
print("Disjoint Sets: ",a.isdisjoint(b))
print()

#Converting List to Set
nums = [1, 2, 2, 3, 3]
s = set(nums)
print(s) # {1, 2, 3}
print()

#Converting Set to List
s = {1, 2, 3}
my_list = list(s)
print(my_list) # [1, 2, 3]
print()

# Frozen Set (Immutable Set) : You cannot modify a frozenset.
fs = frozenset([1, 2, 3])
print(fs) # frozenset({1, 2, 3})
print(type(fs)) # <class 'frozenset'>
