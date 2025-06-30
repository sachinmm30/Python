        #tuples in python
genders=("male", "female", "others")
gender=("Male",) #creating tuple with a one element
print(genders)
print(type(genders))
print(len(genders))
print(gender)
#slicing tuple
print(genders[1:2])
        #Tuple Operation
#Tuple concatination
fruits_tuple=("Apple","banana", "cherry")
vegetable_tuple=("Carrot", "beetroot", "tomato")
combined_tuple= fruits_tuple + vegetable_tuple
print(combined_tuple)

#Tuple repitition
repeat_tuple=(1, 2, 3)*2
repeat_name_tuple=("virat", "kohli", "goat")*2
print(repeat_tuple)
print(repeat_name_tuple)

#Tuple Checking membership
print("Apple" in fruits_tuple)
print("cucumber" in vegetable_tuple)

        #tuple methods
    #Count()
my_tuple=(1,2,3,4,1,1)
print(my_tuple.count(1))
    #index()
my_tuple1=("dog", "cat", "elephant")
print(my_tuple1.index("elephant"))

                        #SETS IN PYTHON
#my_set = {element1, element2, element3, ...}
# Example:
# fruits_set = {"apple", "banana", "cherry"}
# numbers_set = {1, 2, 3, 4, 5}
# Empty Set:
# To create an empty set, use the set() function (not {}, which creates an empty dictionary).

# empty_set = set()

    #set Operation
set1={1,2,3}
set2={3,4,5}    
#union
#union_set= set1 | set2
#print(union_set)
print(set1 | set2)

#intersection
# intersection_set = set1 & set2
# print(intersection_set)
print(set1 & set2)

#Difference
# difference_set = set1 - set2
# print(difference_set)
print(set1 - set2)

#Symmetric difference
# sym_diff_set = set1 ^ set1
# print(sym_diff_set)
print(set1 ^ set2)

    #Set methods
# add(): Adds an element to the set.

fruits_set={"Apple", "banana", "Cherry"}
fruits_set.add("orange")
print(fruits_set)  # Output: {'apple', 'banana', 'cherry', 'orange'}
#remove(): Removes a specified element from the set. Raises an error if the element does not exist.

fruits_set.remove("banana")
print(fruits_set)  # Output: {'apple', 'cherry'}

#discard(): Removes a specified element without raising an error if it does not exist.
fruits_set.discard("banana")  # No error if "banana" is not in the set

# pop(): Removes a random element from the set.
S=fruits_set.pop()
print(S)

# clear(): Removes all elements from the set.
T=fruits_set.clear()
print(T) 