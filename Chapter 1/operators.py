# 🐍 Operators, For Loop, While Loop Demo

# ==============================
# 🔢 OPERATORS IN PYTHON
# ==============================

a = 10
b = 3

# Arithmetic Operators
print("Arithmetic Operators:")
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a % b =", a % b)
print("a ** b =", a ** b)
print("a // b =", a // b)

# Comparison Operators
print("\nComparison Operators:")
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

# Logical Operators
print("\nLogical Operators:")
x = True
y = False
print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)

# Assignment Operators
print("\nAssignment Operators:")
c = 5
c += 2
print("c += 2 ->", c)
c *= 3
print("c *= 3 ->", c)

# ==============================
# 🔁 FOR LOOP
# ==============================

print("\nFor Loop Examples:")

# Print numbers 1 to 5
for i in range(1, 6):
    print("Number:", i)

# Loop through a list
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print("Fruit:", fruit)

# ==============================
# 🔄 WHILE LOOP
# ==============================

print("\nWhile Loop Example:")

count = 1
while count <= 5:
    print("Count:", count)
    count += 1

# ==============================
# 🔚 BREAK & CONTINUE
# ==============================

print("\nBreak Example:")
for i in range(1, 6):
    if i == 3:
        break
    print(i)

print("\nContinue Example:")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)