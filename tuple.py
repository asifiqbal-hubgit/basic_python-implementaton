#Access Tuple Items
#You can access tuple items by referring to the index number, inside square brackets:
employee = ("Asif Iqbal", "Male", 33, "Marketing", 741, "Confiz", "Lahore")
print("Name:", employee[0])
print("Gender:", employee[1])
print("Age:", employee[2])
print("Department:", employee[3])
print("Code:", employee[4])
print("Office:", employee[5])
print("Place:", employee[6])

print(len(employee))
print(type(employee))
#Use slicing:
print(employee[3])
print(employee[2:5])
print(employee[:4])
print(employee[-2])
print(employee[-2:-6])

#Check if Item Exists
#To determine if a specified item is present in a tuple use the in keyword:
employee = ("Asif Iqbal", "Male", 33, "Marketing", 741, "Confiz", "Lahore")
if "Marketing" in employee:
    print("Yes, 'Marketing' is in the employee tuple")
else:
    print("No, 'Marketing' is in the employee tuple")
 # Employee detail in "Tuple".
#Change Tuple Values
#Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
#But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
tuple1 = ("Asif Iqbal", "Male", 33, "Marketing", 741, "Confiz", "Lahore")
tuple2 = list(tuple1)
tuple2[2] = 30
tuple1 = tuple(tuple2)
print(tuple1)

#Add Items
#Since tuples are immutable, they do not have a built-in append() method, but there are other ways to add items to a tuple.
tuple1 = ("Asif Iqbal", "Male", 33, "Marketing", 741, "Confiz", "Lahore")
tuple2 = list(tuple1)
tuple2.append("Developers")
tuple1 = tuple(tuple2)
print(tuple1)

#Remove Items
#Convert the tuple into a list, remove "apple", and convert it back into a tuple:
tuple1 = ("Asif Iqbal", "Male", 33, "Marketing", 741, "Confiz", "Lahore")
tuple2 = list(tuple1)
tuple2.remove("Marketing")
tuple1 = tuple(tuple2)
print(tuple1)

#Or you can delete the tuple completely:
#The del keyword can delete the tuple completely:
tuple1 = ("Asif Iqbal", "Male", 33, "Marketing", 741, "Confiz", "Lahore")
del tuple1
print("tuple1")
#Packing and Unpacking a Tuple
#When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
person = ("Asif Iqbal", "Male", 33, "Marketing")
print(person)
# or simply
person = "Asif Iqbal", "Male", 33, "Marketing"
#Tuple Unpacking
person = ("Asif Iqbal", "Male", 33, "Marketing")
name, gender, age, department = person
print(name)
print(gender)
print(age)
print(department)

#Using Asterisk*
person = ("Asif", "Male", 33, "Marketing", "Pakistan")
name, gender, *details = person
print(details)

#Example with Asterisk on Other Side
#You can also collect the first few items and group the rest:
number = (1, 2, 3, 4, 5)
first, *middle, last = number
print(first)
print(middle)
print(last)

#Tuple for loop
person = ("Asif Iqbal", "Male", 32, "Marketing", "Confiz", "Lahore")
for item in person:
    print(item)
#Using a for Loop with Index
person = ("Asif Iqbal", "Male", 32, "Marketing", "Confiz", "Lahore")
for i in range(len(person)):
    print(f"Index {i}: {person[i]}")
    
#Using enumerate()
person = ("Asif Iqbal", "Male", 32, "Marketing", "Confiz", "Lahore")
for index, value in enumerate(person):
    print(f"{index}: {value}")

#Using a while Loop
i = 0
while i < len(person):
    print(person[i])
    i += 1
#Example with Conditional Logic
#You can combine loops with conditions.
#Example: print only string values.
person = ("Asif Iqbal", "Male", 32, "Marketing", "Confiz", "Lahore")
for item in person:
    if isinstance(item, str):
        print(item)
#Python - Join Tuples
data1 = ("Asif IQbal", "Male", 32)
data2 = ("Confiz", "Simplicant", "Martketing", 741)

joined_data = data1 + data2
print(joined_data)

#Join Multiply Tuples
tuple1 = (10, 20, 30)
tuple2 = (40, 50, 60)
tuple3 = (70, 80, 90)

joined_tuple = tuple1 + tuple2 + tuple3
print(joined_tuple)

#Multiply Tuples using asterisk *
name = ("Asif", "Asad", "Ali") 
result = name * 2
print(result)

#Using sum() Function
#If you have a list of tuples, you can join them all using sum() — but you must start with an empty tuple ().
tuple = [(10, 20), (30, 40), (50, 60)]
result = sum(tuple, ())
print(result)

#Using a Loop
#You can also join tuples in a loop:
tuple = [(10, 20), (30, 40), (50, 60)]
result = ()
for t in tuple:
    result += t
    print(result)