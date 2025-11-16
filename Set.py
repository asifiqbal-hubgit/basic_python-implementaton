


#Using set() constructor
numbers = set([1, 2, 3, 4])
print(numbers)

#Key Features: 
#No duplicates 
my_set = {10, 20, 20, 30, 40, 50}
print(my_set)
#No indexing: sets are unordered and not subscriptable.
# To get an arbitrary element, convert to a list or use an iterator:
first_elem = next(iter(my_set))
print("An element from the set (order arbitrary):", first_elem)
#Length of a Set
my_set = {10, 20, 20, 30, 40, 50}
print(len(my_set))
#type()
my_set = {10, 20, 20, 30, 40, 50}
print(type(my_set))
#String, int and boolean data types:
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(set1)
print(set2)
print(set3)
#A set with strings, integers and boolean values:
thisset = {"Asif", 32, "true", 50, "Male"}
print(thisset)
#Add Elements
#add() → add one item
set_person = {"Asif Iqbal", "Age", "Gender", "Working"}
set_person.add("Contect")
print(set_person)
#Add elements from tropical into thisset:
city_set = {"Islamabad", "Lahore", "Karachi"}
tropical = {"Multan", "Peshawar", "Rawalpindi"}
city_set.update(tropical)
print(city_set)
#update() → add many items
set_person = {"Asif Iqbal", "Age", "Gender", "Working"}
set_person.update(["Contect", "Email", "Address"])
print(set_person)
#Remove Elements: To remove an item in a set, use the remove(), or the discard() method.
#remove() → removes item, gives error if missing
set_person = {"Asif Iqbal", "Age", "Gender", "Working","Contect", "Address", "Email"}
set_person.remove("Address")
print(set_person)
#discard() → removes item, no error if missing
set_person = {"Asif Iqbal", "Age", "Gender", "Working","Contect", "Address", "Email"}
set_person.discard("Phone")
print(set_person)
#pop() → removes a random item
set_person = {"Asif Iqbal", "Age", "Gender", "Working","Contect", "Address", "Email"}
item = set_person.pop()
print("Removed:", item)
print("Remaining:", set_person)
#clear() → removes all items
set_person = {"Asif Iqbal", "Age", "Gender", "Working","Contect", "Address", "Email"}
item = set_person.clear()
print(set_person)
#The del keyword will delete the set completely:
set_person = {"Asif Iqbal", "Age", "Gender", "Working","Contect", "Address", "Email"}
del set_person
try:
    print(set_person)
except NameError:
    print("set_person has been deleted; variable no longer exists")
#Loop Through a Set
number = {10, 20, 30, 40, 50}
for item in number:
    print(item)
#Check If Item Exists In a set:
number = {10, 20, 30, 40, 50}
if 20 in number:
    print("Yes, 20 is in the set")
    if 60 not in number:
        print("No, 60 is not in the set")
#
munber = {10, 20, 30, 40, 50}
print(20 in number)
print(60 not in number)
#Join Sets
#There are several ways to join two or more sets in Python.

#The union() and update() methods joins all items from both sets.

#The intersection() method keeps ONLY the duplicates.

#The difference() method keeps the items from the first set that are not in the other set(s).

#The symmetric_difference() method keeps all items EXCEPT the duplicates.
#Using union() method 1
set1 = {"A", "B", "C"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
#Using update() method 2
set1 = {"A", "B", "C"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)
#Join Multiple Sets
set1 = {1, 2}
set2 = {3, 4}
set3 = {5, 6}
set4 = {7, 8}

myset = set1.union(set2, set3, set4)
print(myset)
#using the | operator
set1 = {1, 2}
set2 = {3, 4}
set3 = {5, 6}
set4 = {7, 8}

myset = set1 | set2 | set3 | set4
print(myset)
#Using update() method
set1 = {1, 2, 3}
set2 = {4, 5,6}
set1.update(set2)
print(set1)
#Using Intersection and & operator
set1 = {"A", "B", "C", "D"}
set2 = {"B", "D", "E", "F"}
set3 = set1 & set2
print(set3)
#Using intersection() method
set1 = {"A", "B", "C", "D"}
set2 = {"B", "D", "E", "F"}
set3 = set1.intersection(set2)
print(set3)
#Using intersection_update() method
set1 = {"A", "B", "C", "D"}
set2 = {"B", "D", "E", "F"}
set1.intersection_update(set2)
print(set1)
#Using difference() method
set1 = {"A", "B", "C", "D"}
set2 = {"B", "D", "E", "F"}
set3 = set1.difference(set2)
print(set3)
#Using - operator
set1 = {"A", "B", "C", "D"}
set2 = {"B", "D", "E", "F"}
set3 = set1 - set2
print(set3)
#Using difference_update() method
set1 = {"A", "B", "C", "D"}
set2 = {"B", "D", "E", "F"}
set1.difference_update(set2)
print(set1)
#Using symmetric_difference() method
set1 = {"A", "B", "C", "D"}
set2 = {"B", "D", "E", "F"}
set3 = set1.symmetric_difference(set2)
print(set3)
#Using ^ operator
set1 = {"A", "B", "C", "D"}
set2 = {"B", "D", "E", "F"}
set3 = set1 ^ set2
print(set3)
#Using symmetric_difference_update() method
set1 = {"A", "B", "C", "D"}
set2 = {"B", "D", "E", "F"}
set1.symmetric_difference_update(set2)
print(set1)
#Copy a Set
set1 = {"A", "B", "C", "D"}
set2 = set1.copy()
print(set2)
#Or use the set() function to make a copy:
set1 = {"A", "B", "C", "D"}
set2 = set(set1)
print(set2)
#Python frozenset
#frozenset is an immutable version of a set.

#Like sets, it contains unique, unordered, unchangeable elements.

#Unlike sets, elements cannot be added or removed from a frozenset.

#Create a frozenset:
myfrozenset = frozenset([1, 2, 3, 4, 5])
print(myfrozenset)
