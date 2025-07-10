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
    print("Yes, 'propper' is in the random_list")

# Change Item Value
name_list = ["Olive", "Hicks", "Kelly", "Diana", "Russell"]
name_list [2] = "Krista"
print(name_list)

#Change the values "Olive" and "Diana" with the values "Della" and "Mark"
name_list = ["Olive", "Hicks", "Kelly", "Diana", "Russell"]
name_list [1:3] = ["Della", "Mark"]
print(name_list)

#The insert() method inserts an item at the specified index:
name_list = ["Olive", "Hicks", "Kelly", "Diana", "Russell"]
name_list.insert(2, "Mark")
print(name_list)

#Append Items
#To add an item to the end of the list, use the append() method & only accepts one argument at a time:
list_cities = ["Lahore", "Islamabad", "Karachi", "Multan"]
list_cities.append("Rawalpindi")
list_cities.append("Gujranwala")
print(list_cities)

#Extend List
#Use extend() to add multiple items at once:
list_cities = ["Lahore", "Islamabad", "Karachi", "Multan"]
list_cities.extend(["Rawalpindi", "Gujranwala", "Faisalabad"])
print(list_cities)

#Add the elements of tropical to thislist:
mobile_name = ["Samsung", "Apple", "Oppo",] 
tropical = ["Nokia", "Vivo", "Huawei"]
mobile_name.extend(tropical)
print(mobile_name)

#Add element of a tuple to a list
this_list = [10, 20, 30, 40, 50]
this_tuple = [60, 70, 80, 90, 100]
this_list.extend(this_tuple)
print(this_list)

#The remove() method removes the specified item and first occurrence in the list
thislist = ["Asif", "Awais", "kamran", "Asad", "Rashid"]
thislist.remove("kamran")
print(thislist)

#First occurrence
thislist = ["Asif", "Awais", "kamran", "Asad", "Rashid", "kamran"]
thislist.remove("kamran")
print(thislist)

#The pop() method removes the specified index.
book_list = ["English", "Urdu", "Math", "Pak-study", "Bio"]
book_list.pop(2)
print(book_list)

book_list = ["English", "Urdu", "Math", "Pak-study", "Bio"]
book_list.pop()
print(book_list)

#The del keyword also removes the specified index:
book_list = ["English", "Urdu", "Math", "Pak-study", "Bio"]
del book_list[1]
print(book_list)

#The del keyword can also delete the list completely.

book_list = ["English", "Urdu", "Math", "Pak-study", "Bio"]
del book_list # This deletes the entire list

#Clear the list content:
book_list = ["English", "Urdu", "Math", "Pak-study", "Bio"]
book_list.clear()
print(book_list) # Output: []

#Loop

numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number * 2)