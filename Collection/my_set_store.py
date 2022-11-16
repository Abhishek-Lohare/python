# 3)  Create a program named "my_set_store" which support following operations on two sets
#     provided by user
#
# for ex:
# 	A = {1,2,3,4,5}
# 	B = {18,19,20,21}
# is provided by the user
# Operations supported by our program are :
# 	1: Union
# 	2: Intersection
# 	3: A-B
# 	4: B-A
# 	5: Take a element from user and Display if that element is a member of set B
# 	6: Display number of elements in the set A
#     7: Display number of elements in the set B
# 	8: Add an element taken from the user to the set A
# 	9: Add multiple elements taken from the user to the set A
# 	10: Remove an element taken from the user from set A
# ============================================================================================================

a = set()
b = set()

lim_A = int(input("How many elements you want to add into setA: "))
for i in range(0, lim_A):
    ele_a = int(input("Enter the element: "))
    a.update({ele_a})
lim_B = int(input("How many elements you want to add into setB: "))
for i in range(0, lim_B):
    ele_b = int(input("Enter the element: "))
    b.update({ele_b})
print('elements of Set A: ', a)
print('elements of Set B: ', b)
# ===========================================================================================================
# Operations supported by our program are :
#1: Union
print("Union is : ", a.union(b))
# ===========================================================================================================
#2: Intersection
print("Intersection is :", a.intersection(b))
# ===========================================================================================================
#3: A-B
print("A-B", a - b)
# ===========================================================================================================
#4: B-A
print("B-A", b - a)
# ===========================================================================================================
#5: Take a element from user and Display if that element is a member of set B
num = int(input("Enter the element to check with set B: "))
check = num in b
if check:
    print("Entered element is member of B")
else:
    print("Entered element is not a member of B")
# ===========================================================================================================
#6: Display number of elements in the set A
print("Elements of Set A: ", a)
#7: Display number of elements in the set B
print("Elements of Set B: ", b)
# ===========================================================================================================
#8: Add an element taken from the user to the set A
add_ele = int(input("Enter the element to add into setA: "))
a.add(add_ele)
print("Element", add_ele, " is added into list A!! ", a)
# ===========================================================================================================
#9: Add multiple elements taken from the user to the set A
lim_n = int(input("How many elements you want to add into setA: "))
for i in range(0, lim_n):
    ele_new = input("Enter the element: ")
    if ele_new.isdigit():
        a.add(int(ele_new))
    else:
        a.add(ele_new)
print("Updated set A ", a)
# ===========================================================================================================
# 10: Remove an element taken from the user from set A
del_ele = input("Enter the element to delete from setA: ")
if del_ele.isdigit() or del_ele in a:
    a.discard(int(del_ele))
elif del_ele in a:
    a.discard(del_ele)
else:
    print("element is not present")

print("Updated Set A: ", a)
# ===========================================================================================================





# if del_ele in a:
#     if del_ele.isdigit():
#         a.discard(int(del_ele))
#     else:
#         a.discard(del_ele)
# else:
#     print("Element not present in the Set A")
#
# print("Updated Set A: ", a)
