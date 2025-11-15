


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
