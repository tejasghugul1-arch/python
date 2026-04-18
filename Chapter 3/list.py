list = ["apple","oarange",1,True]
list[0] = "tejas"# only can change before printing 
list.append("oranges")#add at the end 
l1 =[12,3,56]
l1.sort()
l1.reverse()
l1.insert(1(#indexno),33333(no to be insert))
l1.pop(3)#exclude3 element on index 
l1.remove(2)#remeove elements 
print(l1.pop(3))#will print element at index 2
print(l1)
print(list[4])


# ehen u call items always use reactangle brackets list always have rectangle braclets
# we wer not able to to have change in strings beacse they were immutable
#but in list we can 
# list is mustable
# 🐍 Python Lists – Concepts & Properties

## 📌 What is a List?

# A **list** is a collection of items stored in a single variable.

# ```python
# numbers = [1, 2, 3, 4]
# ```

# * Can store multiple values
# * Items are separated by commas
# * Enclosed in square brackets `[]`

# ---

# ## 🔑 Properties of Lists

# ### 1️⃣ Ordered

# Items have a defined order and index (starting from 0)

# ```python
# fruits = ["apple", "banana", "mango"]
# print(fruits[0])  # apple
# ```

# ---

# ### 2️⃣ Mutable (Changeable)

# You can modify list elements

# ```python
# fruits[1] = "orange"
# print(fruits)
# ```

# ---

# ### 3️⃣ Allows Duplicates

# ```python
# nums = [1, 2, 2, 3]
# ```

# ---

# ### 4️⃣ Heterogeneous (Different Data Types)

# ```python
# data = [10, "hello", 3.5, True]
# ```

# ---

# ### 5️⃣ Dynamic Size

# You can add/remove elements anytime

# ---

# ## ⚙️ Common List Operations

# ### ➕ Add Elements

# ```python
# lst = [1, 2, 3]
# lst.append(4)        # add at end
# lst.insert(1, 10)    # insert at index
# ```

# ---

# ### ➖ Remove Elements

# ```python
#---------------- lst.remove(2)   # remove value
# lst.pop()       # remove last
# del lst[0]      # delete by index
# ```

# ---

# ### 🔍 Access Elements

# ```python
# lst = [10, 20, 30]
# print(lst[1])      # 20
# print(lst[-1])     # 30 (last element)
# ```

# ---

# ### 🔄 Slicing

# ```python
# lst = [1, 2, 3, 4, 5]
# print(lst[1:4])   # [2, 3, 4]
# ```

# ---

# ### 🔁 Loop Through List

# ```python
# for item in lst:
#     print(item)
# ```

# ---

# ### 📊 Useful Functions

# ```python
# len(lst)      # length
# max(lst)      # maximum value
# min(lst)      # minimum value
# sum(lst)      # sum of elements
# ```

# ---

# ## 📌 Example Program

# ```python
# # List Example
# numbers = [10, 20, 30]

# numbers.append(40)
# numbers.insert(1, 15)

# print("List:", numbers)

# numbers.remove(20)
# print("After removal:", numbers)

# print("Length:", len(numbers))
# print("Max:", max(numbers))
# ```

# ---

# ## 📌 Summary

# * Lists are ordered and mutable
# * Can store different data types
# * Supports indexing and slicing
# * Very useful for storing collections of data

# ---

# 💡 *Lists are one of the most important data structures — master them well!* 🚀
