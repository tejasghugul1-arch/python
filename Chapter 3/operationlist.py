# 🐍 All List Operations in Python

# ==============================
# 📌 CREATE LIST
# ==============================
l1 = [10, 20, 30, 40]
print("Original List:", l1)

# ==============================
# 🔍 ACCESS ELEMENTS
# ==============================
print("First element:", l1[0])
print("Last element:", l1[-1])

# ==============================
# ✏️ MODIFY ELEMENT
# ==============================
l1[1] = 25
print("After modification:", l1)

# ==============================
# ➕ ADD ELEMENTS
# ==============================
l1.append(50)             # add at end
print("After append:", l1)

l1.insert(2, 15)          # insert at index
print("After insert:", l1)

l1.extend([60, 70])       # add multiple elements rectangle brackets
print("After extend:", l1)

# ==============================
# ➖ REMOVE ELEMENTS
# ==============================
l1.remove(25)             # remove value      aelement
print("After remove:", l1)

l1.pop()                  # remove last
print("After pop:", l1)

l1.pop(2)                 # remove by index  index
print("After pop index:", l1)

del l1[0]                 # delete by index
print("After del:", l1)

# ==============================
# 🔄 SLICING
# ==============================
l2 = [1, 2, 3, 4, 5]
print("Slice [1:4]:", l2[1:4])
print("Reverse:", l2[::-1])

# ==============================
# 🔁 LOOP THROUGH LIST
# ==============================
print("Looping:")
for i in l2:
    print(i)

# ==============================
# 📊 LIST FUNCTIONS
# ==============================
nums = [5, 2, 9, 1]

print("Length:", len(nums))
print("Max:", max(nums))
print("Min:", min(nums))
print("Sum:", sum(nums))

# ==============================
# 🔃 SORTING
# ==============================
nums.sort()
print("Sorted:", nums)

nums.sort(reverse=True)
print("Descending:", nums)

# ==============================
# 🔁 COPY LIST
# ==============================
copy_list = nums.copy()
print("Copied List:", copy_list)

# ==============================
# 🔍 SEARCH ELEMENT
# ==============================
print("Index of 5:", nums.index(5))

# ==============================
# 🔢 COUNT ELEMENT
# ==============================
nums2 = [1, 2, 2, 3]
print("Count of 2:", nums2.count(2))

# ==============================
# 🧹 CLEAR LIST
# ==============================
nums2.clear()
print("After clear:", nums2)

# ==============================
# 🔗 CONCATENATION
# ==============================
a = [1, 2]
b = [3, 4]
c = a + b
print("Concatenated:", c)

# ==============================
# 🔁 REPETITION
# ==============================
print("Repetition:", a * 3)