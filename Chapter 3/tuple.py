#tuple () 
a = (1,)#(1)s not tuple
print(type(a))
#tupple immutable
#fast than list

t = (1, 2, 3)
print(t[0])   # 1
print(t[-1])  # 3
print(t[0:2])   # (1, 2)   starty end
t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2)   # (1, 2, 3, 4)
print(t * 2)   # (1, 2, 3, 1, 2, 3)
print(2 in t)   # True
print(len(t))   # 3
t = (1, 2, 2, 3)
print(t.count(2))   # 2
print(t.index(3))   # 3rd position → index 3
for i in t:
    print(i)