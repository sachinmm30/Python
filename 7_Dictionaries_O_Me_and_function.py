#Creating dictionary in python

birthday ={
    "sachin": "30/08/200",
    "likith": "25/09/2002",
    "bob":"27/05/2002"
}
        #Accessing dictionary elements
print(birthday)
print(birthday["likith"])
print(birthday.get("bob")) 
print(birthday.get("Abhi"))  #by using get.(), which is safer because it doesn’t throw an error if the key doesn’t exist.

        #Adding and Updating Dictionary Elements
birthday["Abhi"]="26/05/2002"
print(birthday)

        #Removing Elements from a Dictionary
karnataka_food = {
    "Bengaluru": "Bisi Bele Bath",
    "Mysuru": "Mysore Pak",
    "Mangaluru": "Neer Dosa"
}
#pop(): Removes the specified key and returns the associated value.
mysuru_food = karnataka_food.pop("Mysuru")
print(mysuru_food)  # Output: Mysore Pak

#del: Removes the specified key.
del karnataka_food["Mangaluru"]

#clear(): Empties the dictionary.
a = karnataka_food.clear()
print(a)

        #Dictionary Methods
    #key() returns all the keys in dictionary

karnataka_food1 = {
    "Bengaluru": "Bisi Bele Bath",
    "Mysuru": "Mysore Pak",
    "Mangaluru": "Neer Dosa"
}
print(karnataka_food1.keys())

    #value() returns all values
print(karnataka_food1.values())

    #items() returns key-value pair as tuples
print(karnataka_food1.items())

    #update() : updates the dictionary with another dictionary
new_dishes={"hubballi" : "girmit", "dharwad" : "peda", }
karnataka_food1.update(new_dishes)
print(karnataka_food1)

#EXTRA
item1={
    "name" : "Milk",
    "weight": 1,
    "price" : 5
}
item2={
    "name": "sugar",
    "weight": 2,
    "price": 99.99
}

items=[item1, item2]
print(items)
print(f"total Weight: {item1["weight"] + item2["weight"]}Kg")
print(f"total Weight: {item1["name"] + " "+item2["name"]}")