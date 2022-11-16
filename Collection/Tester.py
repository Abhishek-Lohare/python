#   1:  Display number of elements in the members list
#   2:  Add an element to the members collection like 'Sehwag'
#   3:  Add elements to the members collection like ['David','Bret','Sanju']
#   4:  Remove a member from the collection at a given subscript
#   5:  Remove the last member from the collection
#   6:  Display third, fourth and fifth element from the collection
#
# Keep asking the user for the operation in this store until he chooses to exit from the program
import assignment_06

assignment_06.create_list()

flag = True
while flag:
    choice = int(input("Enter your choice : "
                       "\n1.Display number of elements"
                       "\n2.Add single element to the members"
                       "\n3.Add multiple elements to the members"
                       "\n4.Remove a member from the collection at a given subscript"
                       "\n5.Remove the last member from the collection"
                       "\n6.Display third, fourth and fifth element from the collection"))
    if choice == 1:
        assignment_06.no_of_elements()
    elif choice == 2:
        assignment_06.add_an_element()
    elif choice == 3:
        assignment_06.add_multi_element()
    elif choice == 4:
        assignment_06.remove_ele()
    elif choice == 5:
        assignment_06.remove_last()
    elif choice == 6:
        assignment_06.display_selected()
    else:
        print("Incorrect Inout please try again!!!")

    check = input("Do you want to continue : (Y/N)").lower()
    if check == 'y':
        continue
    elif check == 'n':
        print("Exited from the Game!!"
              "\nThank You!!")
        flag = False
        break

"""
flag = True
looping = False
while flag:
    if looping:
        check = input("Do you want to continue with this game(Y/N)").lower()
        if check == 'y':
            choice = int(input("Enter your choice : "
                               "\n1.Display number of elements"
                               "\n2.Add single element to the members"
                               "\n3.Add multiple elements to the members"
                               "\n4.Remove a member from the collection at a given subscript"
                               "\n5.Remove the last member from the collection"
                               "\n6.Display third, fourth and fifth element from the collection"))
            if choice == 1:
                assignment_06.no_of_elements()
                looping = True
            elif choice == 2:
                assignment_06.add_an_element()
                looping = True
            elif choice == 3:
                assignment_06.add_multi_element()
                looping = True
            elif choice == 4:
                assignment_06.remove_ele()
                looping = True
            elif choice == 5:
                assignment_06.remove_last()
                looping = True
            elif choice == 6:
                assignment_06.display_selected()
                looping = True
            else:
                print("Incorrect Inout please try again!!!")
                looping = True

        elif check == 'n':
            print("Exited from the Game!!\nThank You!!")
            flag = False
            break
        else:
            print("Incorrect Input!")
            looping = True
            continue
"""
