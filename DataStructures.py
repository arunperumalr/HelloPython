# ********************** LIST **********************

list01 = [1, 3, 5, 7, 9]
list02 = [2, 4, 6, 8, 10]
list03 = ['a', 1, [1,2]]

# PRINTS : list01 Length =  5
print("list01 Length = ", len(list01))
print()

# PRINTS : Number of times two has occurred in list02 =  1
print("Number of times two has occurred in list02 = ", list.count(list02, 2))
print()

# PRINTS : Appended list01 and list02:  [1, 3, 5, 7, 9, 11] [2, 4, 6, 8, 10, 12]
list01.append(11)
list02.append(12)
print("Appended list01 and list02: ", list01, list02)
print()

# PRINTS : Deleted list01 and list02:  [1, 3, 5, 7, 9] [2, 4, 6, 8, 10]
list01.remove(11)
del list02[5]
print("Deleted list01 and list02: ", list01, list02)
print()

# PRINTS : Reversed list01:  [9, 7, 5, 3, 1]
list01.reverse()
print("Reversed list01: ", list01)
print()

# PRINTS : Sorted list01:  [1, 3, 5, 7, 9]
list01.sort()
print("Sorted list01: ", list01)
print()

# PRINTS : Extended list01:  [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
list01.extend(list02)
print("Extended list01: ", list01)
print()

# PRINTS : list01 after removing list02:  [1, 3, 5, 7, 9]
for item in list02:
    list01.remove(item)
print("list01 after removing list02: ", list01)
print()

# PRINTS : Complex list03 :  ['a', 1, [1, 2]]
print("Complex list03 : ",list03)

# ********************** LIST **********************