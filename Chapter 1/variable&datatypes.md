# 🐍 Python – Variables & Data Types

## 📌 Variables in Python

A variable is a **name used to store data** in memory.

### ✅ Example:

```python
x = 10
name = "Tejas"
pi = 3.14
```

* No need to declare type (Python is **dynamically typed**)
* Type is decided automatically at runtime

---

## 🔑 Rules for Naming Variables

* Must start with a letter or underscore (`_`)
* Cannot start with a number ❌
* Cannot use keywords (`if`, `for`, `while`, etc.)
* Case-sensitive (`age` and `Age` are different)

---

## 📦 Multiple Assignments

```python
a, b, c = 1, 2, 3
x = y = z = 0
```

---

## 🔄 Type Checking

```python
x = 10
print(type(x))  # <class 'int'>
```

---

## 🔤 Data Types in Python

### 1️⃣ Integer (int)

Whole numbers (positive/negative)

```python
a = 10
b = -5
```

---

### 2️⃣ Float (float)

Decimal numbers

```python
pi = 3.14
temp = -2.5
```

---

### 3️⃣ String (str)

Text data (inside quotes)

```python
name = "Python"
msg = 'Hello'
```

---

### 4️⃣ Boolean (bool)

True or False values

```python
is_valid = True
is_done = False
```

---

### 5️⃣ List (list)

Ordered, mutable collection

```python
numbers = [1, 2, 3, 4]
```

---

### 6️⃣ Tuple (tuple)

Ordered, immutable collection

```python
coords = (10, 20)
```

---

### 7️⃣ Set (set)

Unordered, unique elements

```python
unique = {1, 2, 3}
```

---

### 8️⃣ Dictionary (dict)

Key-value pairs

```python
student = {
    "name": "Tejas",
    "age": 20
}
```

---

## 🔁 Type Conversion (Casting)

```python
x = "10"
y = int(x)   # convert string to int
z = float(y)
```

---

## ⚡ Important Points

* Python is **dynamically typed**
* Variables don’t need explicit declaration
* Data types can change at runtime

```python
x = 10
x = "hello"//string
```

---

## 📌 Summary

* Variables store data values
* Python automatically assigns data types
* Supports multiple built-in data types
* Flexible and easy to use

---

💡 *Practice daily and push your progress to GitHub!* 🚀
