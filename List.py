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

#For Loop

numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number * 2)

for i in range(10):
    print(i)

#While loop
i = 0
while i < 5:
    print(i)
    i += 1

#Loop: Print all items in the list, one by one:
python = ["List", "Tuples", "Sets", "Dictionaries"]
for x in python:
    print(x)

#Use the range() and len() functions to create a suitable iterable.
#Print all items by referring to their index number
python = ["List", "Tuples", "Sets", "Dictionaries"]
for i in range(len(python)):
    print(python[i])

#Using While loop
python = ["1: List", "2: Tuples", "3: Sets", "4: Dictionaries", "5: Data Type", "6: Variable"]
i = 0
while i < len(python):
     print(python[i])
     i = i + 1

# Looping Using List Comprehension
python = ["1) List", "2) Tuples", "3) Sets", "4) Dictionaries", "5) Data Type", "6) Variable"]
[print(x) for x in python]

#List Comprehension
#Example
newList = [i for i in range(0,20)]
print(newList)

#Example
squares = [x**2 for x in range(5)]
print(squares)
# Output: [0, 1, 4, 9, 16]

#List of even numbers
evens = [x for x in range(10) if x % 2 == 0]
print(evens)

#Nesting list comprehensions
my_matrix = [[j * 2 for j in range (1,5)] for i in range (1,5)]
print (my_matrix)

#Set the values in the new list to upper case
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x.upper() for x in fruits]

print(newlist)

#Sort List(Numerically)
number = [30, 10, 80, 50, 20, 70, 40, 100, 90, 60]
number.sort()
print(number)

#Sort Descending
number = [30, 10, 80, 50, 20, 70, 40, 100, 90, 60]
number.sort(reverse=True)
print(number)

##Sort List(Alphanumerically)

list_alphanumerically = ["List", "Tuples", "Sets", "Dictionaries"]

list_alphanumerically.sort()

print(list_alphanumerically)

#Using sorted()
numbers = [4, 1, 3, 9, 2]
sorted_list = sorted(numbers)
print(sorted_list)

#Copy a List
#Use the copy() method
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
vegelist = vegetables.copy()
print(vegelist)

#Using List Slicing
original = [1, 2, 3, 4, 5]
copying = original[:]

print(copying)

#Join Two Lists

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

list3 = list1 + list2
print(list3)

# Join by extend method
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

list1.extend(list2)
print(list1)

# Using loop
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = []

for item in list1:
    combined.append(item)

for item in list2:
    combined.append(item)

print(combined)