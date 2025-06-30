item1 = "bru"
item2= "sugar"
item3= "milk"

items=["bru", "sugar", "milk", "soppu", "kaalu"]
print(item1, item2, item3)
print(items[0])
print(items[-1])

    #Modifying list
cars=["swift", "BMW", "Volvo"]
cars[0]="Tesla"
print(cars)

    #1 Adding elements to list
fruits=["Apple", "Banana", "Cherry"]
print(fruits)

fruits.append("Grapes")
print(fruits)

fruits.insert(0, 100)
print(fruits)

    #2 Removing elements in a list
cities=["mysore", "mandya", "bengalore"]
cities.remove("mandya")
print(cities) #o/p ['mysore', 'bengalore']

towns=["KRN", "HUN", "MYS"]
towns.pop()
print(towns) #o/p []

towns.pop(0)
print(towns)

    #Slicing lists
numbers = [0, 1, 2, 3, 4, 5, 6]
print(numbers[1:4])  # Output: [1, 2, 3] (from index 1 to 3)
print(numbers[:4])  # Output: [0, 1, 2, 3] (from start to index 3)
print(numbers[2:])  # Output: [2, 3, 4, 5, 6] (from index 2 to end)
print(numbers[::2])  # Output: [0, 2, 4, 6] (every 2nd element)


    #Lists function and method
    #common functions
#len(list)
companies=["Wipro", "texas", "infosys" ]
print(len(companies))
#sorted(list)
numbers = [5, 2, 9, 1]
print(sorted(numbers))
#sum(list)
numbers = [1, 2, 3, 4]
print(sum(numbers))

    #Common Methods:
cricketors=["virat", "sachin", "rahul", "jadeja"]
#index(element)
print(cricketors.index("rahul"))
#count(element)
print(cricketors.count("virat"))
digits=[1,2,3,2,1,1]
print(digits.count(1))
#reverse
digits.reverse()
print(digits)
#sort()
num=[1,5,8,3]
num.sort()
print(num)