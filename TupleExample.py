# ********************** TUPLE **********************
print("********************** TUPLE **********************")
print("A tuple is an ordered, immutable collection in Python.")
my_tuple = (10, 20, 30, 40)
print("my_tuple : ", my_tuple)
print()

#Normal Tuple
numbers = (1, 2, 3)
print("numbers : ",numbers)
print()

#Single Element Tuple: Comma is mandatory
single = (5)
print(type(single)) # Output : <class 'int'>
print()

single = (5,)
print(type(single)) # Output : <class 'tuple'>
print()

#Without Parentheses
data = 1, 2, 3
print(type(data)) # Output : <class 'tuple'>
print()

#Accessing Elements
t = ("a", "b", "c")

#Indexing
print(t[0]) # Output : a
print(t[1]) # Output : b

#-ve Indexing
print(t[-1]) # Output : c
print()

#Slicing
nums = (10, 20, 30, 40, 50)
print(nums[1:4]) # Output : (20, 30, 40)
print(nums[:3]) # Output : (10, 20, 30)
print(nums[::2]) # Output : (10, 30, 50)
print()

#Tuple Concatenation
t1 = (1, 2)
t2 = (3, 4)
result = t1 + t2
print(result) # Output : (1, 2, 3, 4)
print()

#Tuple Repetition
t = ("Hi",)
print(t * 3) # Output : ('Hi', 'Hi', 'Hi')
print()

#Membership Test
t = (10, 20, 30)
print(20 in t) # Output : True
print(50 not in t) # Output : True
print()

#Iterating Through Tuple
colors = ("red", "green", "blue")

for color in colors:
    print(color)

# Output : red green blue
print()

#Tuple Unpacking : Basic
person = ("Arun", 28, "Chennai")

name, age, city = person

print(name) # Output : Arun
print(age) # Output : 28
print(city) # Output : Chennai
print()

#Tuple Unpacking : Swapping Variables Using Tuple Unpacking
a = 10
b = 20
a, b = b, a
print(a) # Output : 20
print(b) # Output : 10
print()

#Tuple Unpacking : Using * for Multiple Values

numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
print(first) # Output : 1
print(middle) # Output : [2, 3, 4]
print(last) # Output : 5
print()

#Tuple Unpacking : Inside a Loop

students = [
    ("Arun", 85),
    ("Rahul", 90),
    ("Priya", 95)
]

for name, marks in students:
    print(name, marks)

# Output :
# Arun 85
# Rahul 90
# Priya 95
print()

##Tuple Unpacking : Function Returning Multiple Values : Python actually returns them as a tuple.

def get_coordinates():
    return (10, 20)

x, y = get_coordinates()

print(x) # Output : 10
print(y) # Output : 20
print()

#Tuple Length
t = (1, 2, 3, 4)
print(len(t)) # Output : 4
print()

#Count Occurrences
t = (1, 2, 2, 3, 2)
print(t.count(2)) # Output : 3
print()

#Find Index
t = (10, 20, 30)
print(t.index(20)) # Output : 1
print()

#Nested Tuples
nested = ((1, 2), (3, 4))
print(nested[1]) # Output : (3, 4)
print(nested[1][0]) # Output : 3
print()

#Converting List to Tuple
my_list = [1, 2, 3]
t = tuple(my_list)
print(t) # Output : (1, 2, 3)
print()

#Converting Tuple to List
t = (1, 2, 3)
my_list = list(t)
print(my_list) # Output : [1, 2, 3]
print()

#Built-in Functions with Tuples
t = (5, 2, 8, 1)

print(min(t))  # Output : 1
print(max(t))  # Output : 8
print(sum(t))  # Output : 16
print(sorted(t))  # Output : [1, 2, 5, 8]
print()

# Using Tuples as Dictionary Keys
locations = {
    (13.08, 80.27): "Chennai",
    (13.08, 80.28): "Blore"
}

print(locations[(13.08, 80.27)]) # Output : Chennai
print(locations[(13.08, 80.28)]) # Output : Blore
print()

#Comparing Tuples
print((1, 2) == (1, 2)) # Output : True
print((1, 2) < (1, 3)) # Output : True
print()

#Deleting a Tuple
t = (1, 2, 3)
del t