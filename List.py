#List creation
mylist_flowers  = ["Rose", "Tulip", "Sunflower", "Daisy", "Marigold", "Jasmine", "lotus"]
print(mylist_flowers )

#Mutable: The elements of the list can be modified. We can add or remove items to the list after it has been created.
#Ordered: The items in the lists are ordered. Each item has a unique index value. The new items will be added to the end of the list.
#Heterogenous: The list can contain different kinds of elements i.e; they can contain elements of string, integer, boolean, or any type.
#Duplicates: The list can contain duplicates i.e., lists can have two items with the same values.

#Allow Duplicates, List Length, 
car_list = ["Toyota", "Honda", "Chevrolet", "BMW", "Ford", "Handa", "BMW"]
print(len(car_list))

#The list() Constructor
furniture_list = (("chairs", "tables", "beds", "sofas", "dressers"))
print(furniture_list)

#Type of list
furniture_list = ["chairs", "tables", "beds", "sofas", "dressers"]
print(type(furniture_list))

#List Items - Data Types
list = ["abc", 123, "Ture", 50,]
print(list)

#Access Items, Negative Indexing
random_list = ["laptop", "book", "mobile", "pen", "box", "dropper", "oil"]
print(random_list[3])
print(random_list[3:5])
print(random_list[:4])
print(random_list[-5])
print(random_list[-2:-5])

#Check if Item Exists
random_list = ["laptop", "book", "mobile", "pen", "box", "dropper", "oil"]
if "dropper" in random_list:
    print("Yes, 'propper'is in the random_list")