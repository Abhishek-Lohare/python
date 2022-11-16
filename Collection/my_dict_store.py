#
# 2) Create a program named "my_dict_store" which support following operations on
# dictionary named "capitals" which would have keys as their country and values as their capitals
# respectively from the user
# for ex: "India" : "New Delhi" ,"USA" : "Washington DC","Nepal": "Kathmandu","Ukraine" : "Kyiv"
# is provided by the user
#
# Operations supported by our program are : 1: Display number of elements in the capitals collection 2: Add an
# element to the capitals collection like --> Afghanistan: Kabul 3: Add multiple elements to the capitals collection
# like -->  Albania:Tirana,Algeria:Algiers,Andorra:Andorra la Vella 4: Remove an element from the collection
#
# Keep asking the user for the operation in this store untill he chooses to exit from the program
# ============================================================================================================================

capitals = {}
rng = int(input("Enter how many elements to add: "))
for i in range(0, rng):
    key = input("Enter the State: ").upper()
    value = input("Enter the capital City: ").upper()
    capitals[key] = value
print(capitals)

flag = True
while flag:
    # ============================================================================================================================
    # 1: Display number of elements in the capitals collection
    print("No of elements in dictionary is : ", len(capitals))
    # ============================================================================================================================
    # 2: Add an element to the capitals collection like --> Afghanistan: Kabul
    key2 = input("To Add new Element \nEnter the State: ").upper()
    value2 = input("Enter the capital City: ").upper()
    capitals[key2] = value2
    print(capitals)
    # ============================================================================================================================
    # 3: Add multiple elements to the capitals collection
    # like -->  Albania:Tirana,Algeria:Algiers,Andorra:Andorra la Vella
    rng = int(input("Enter how many elements to add: "))
    for i in range(0, rng):
        key3 = input("Enter the State: ").upper()
        value3 = input("Enter the capital City: ").upper()
        capitals[key3] = value3
    print(capitals)
    # ============================================================================================================================
    # 4: Remove an element from the collection
    key = input("Enter the key to Remove elements: ").upper()
    capitals.pop(key)
    print(capitals)
    break
