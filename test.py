#ython Dictionaries
#A dictionary in Python is a collection of key-value pairs.
#It is used to store data values like a map — each value is accessed using its key, not an index.
#Key Features
#Unordered (Python 3.7+ maintains insertion order, but conceptually unordered)
#Mutable (you can change it)
#Keys must be unique
#Keys can be strings, numbers, tuples (immutable types)
person = {
    "Name:", "Asif Iqbal",
    "Age:", 30,
    "City:", "New York"
    "Depatment:", "Sales & Marketing"
    "Company:", "Confiz"
}
print(person)
#Dictionary Items
#Print the "brand" value of the dictionary:
mobile = {
    "Brand": "iPhone",
    "Model": "J7 Pro",
    "Year": 2025,
    "Colour": "Gray"
}
print(mobile)

#Duplicates Not Allowed
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
#Find lenth
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(len(thisdict))
#Dictionary Items - Data Types
employee = {
    "Name": "Asif Iqbal",
    "Age": 32,
    "Designation": "GM",
    "Office": "Confiz",
    "City": "Lahore",
    "Job Data": ["Email", "Code", "Department",]
}
print(employee)
print(type(employee)) # For checking the data type of dictionary
#The dict() Constructor
thisdict = dict(Brand="Ford", Model="Mustang", Year=1964)
print(thisdict)
#Accessing Items
#You can access the items of a dictionary by referring to its key name, inside square brackets
employee = {
    "Name": "Asif Iqbal",
    "Age": 32,
    "Designation": "GM",
    "Office": "Confiz",
    "City": "Lahore"
}
employee = {
    "Name": "Asif Iqbal",
    "Age": 32,
    "Designation": "GM",
    "Office": "Confiz",
    "City": "Lahore"
}
print(employee["Name"])
print(employee["Age"])
print(employee["Designation"])
print(employee["Office"])
print(employee["City"])

#You can also use the get() method to access the value of a specific key.
employee = {
    "Name": "Asif Iqbal",
    "Age": 32,
    "Designation": "GM",
    "Office": "Confiz",
    "City": "Lahore"
}
x = employee.get("Age")
print(x)

#Accessing and Modifying the Index
import pandas as pd

data = {'Name': ['John', 'Alice', 'Bob', 'Eve', 'Charlie'],
        'Age': [25, 30, 22, 35, 28],
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'],
        'Salary': [50000, 55000, 40000, 70000, 48000]}

df = pd.DataFrame(data)
print(df.index)  # Accessing the index