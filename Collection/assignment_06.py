# --------------------------------------------------------------------------------------------------------
# Assignment/Exercises
# Topics covered : Modules,Functions,Looping,Conditional constructs,Input,Output,LIST Collections :
# -------------------------------------------------------------------------------------------
# 1) Create a program named "my_list_store"
# which support following operations on list named "members" which is provided by the user
# for ex: ["Pratiksha","Kevin","Sachin","Yuvraj","Sania"] is provided by the user
#
# Operations supported by our program are :
#   1:  Display number of elements in the members list
#   2:  Add an element to the members collection like 'Sehwag'
#   3:  Add elements to the members collection like ['David','Bret','Sanju']
#   4:  Remove a member from the collection at a given subscript
#   5:  Remove the last member from the collection
#   6:  Display third, fourth and fifth element from the collection
#
# Keep asking the user for the operation in this store until he chooses to exit from the program
# =====================================================================================================
members = []


def create_list():
    print("Registering a customer")
    ele = int(input("Enter how many elements you want add to the list"))
    for i in range(0, ele):
        mem_name = input("Enter the names of members: ")
        members.append(mem_name)
    print("Members added in list : \n", members)

print("Inside my_list_store")
#create_list()


# ==================================================================
#   1:  Display number of elements in the members list
def no_of_elements():
    print("Member list has total", len(members), "Members")
#no_of_elements()  # method_Calling


# ==================================================================
#   2:  Add an element to the members collection like 'Sehwag'
def add_an_element():
    add_ele = input("Enter the Name of member: ")
    members.append(add_ele)
    print(members)


#add_an_element()  # method_Calling


# ==================================================================

#   3:  Add elements to the members collection like ['David','Bret','Sanju']
def add_multi_element():
    multi_elements = []
    n1 = int(input("Enter how many elements you want to add"))
    for i in range(0, n1):
        element = input("Enter the Name of Members: ")
        multi_elements.append(element)
    print(multi_elements)
    members.append(multi_elements)
    print(members)


#add_multi_element()  # method_Calling
# =====================================================================================
#print("=====================================================================================")


#   4:  Remove a member from the collection at a given subscript

def remove_ele():
    print("|Index|  |Elements|")
    for i, ele in enumerate(members):
        print(i, ele)

    index = int(input("Enter the index of element you want to "))
    members.pop(index)
    print(members)


#remove_ele()  # Method_calling


# =====================================================================================
#   5:  Remove the last member from the collection
def remove_last():
    members.pop()
    print(members)


# remove_last()
# =====================================================================================
#   6:  Display third, fourth and fifth element from the collection
def display_selected():
    for i in range(3, 6):
        print(members[i])
    # or
    #print(members[4:7])

#display_selected()
