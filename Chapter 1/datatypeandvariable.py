# 🐍 Variables and Data Types Demo

# Integer
age = 20
print("Age:", age, "Type:", type(age))

# Float
height = 5.9
print("Height:", height, "Type:", type(height))

# String
name = "Tejas"
print("Name:", name, "Type:", type(name))

# Boolean
is_student = True
print("Is Student:", is_student, "Type:", type(is_student))

# List (mutable)
numbers = [1, 2, 3, 4]
print("List:", numbers, "Type:", type(numbers))

# Tuple (immutable)
coordinates = (10, 20)
print("Tuple:", coordinates, "Type:", type(coordinates))

# Set (unique values)
unique_values = {1, 2, 3, 3, 2}
print("Set:", unique_values, "Type:", type(unique_values))

# Dictionary (key-value pairs)
student = {
    "name": "Tejas",
    "age": 20,
    "branch": "Electrical"
}
print("Dictionary:", student, "Type:", type(student))

# 🔄 Type Conversion
x = "100"
y = int(x)   # string to int
print("Converted:", y, "Type:", type(y))

# 🔁 Dynamic Typing
var = 10
print("Before:", var, type(var))

var = "Now I am string"
print("After:", var, type(var))