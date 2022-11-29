# 1. Write a Python program that accept a number of words and then those number of words and
# Print the number of distinct words
# and number of occurrences for each distinct word according to their appearance.
# Input the words:
# Red
# Green
# Blue
# Black
# White
# Blue
# Green
#
# Output:
#
# "Number of distinct words are 5"
# Red : 1
# Green: 2
# Blue : 2
# Black : 1
# White : 1
# ============================SOLUTION==============================================
# words_list = ["Red", "Blue", "Green","Black", "White","Blue","Green"]
# word_distinct = set(words_list)
# distinct_list = list(word_distinct)
# print(distinct_list)
# count = 0
# no_of_occurance = []
# for i in distinct_list:
#     for j in words_list:
#         if i == j:
#             count += 1
#     no_of_occurance.append(count)
#     count=0
#
# #res = {test_keys[i]: test_values[i] for i in range(len(test_keys))}
# #my_dict ={stud_list[i]:marks_list[i] for i in range(len(stud_list))}
# new_dict= {distinct_list[i]:no_of_occurance[i] for i in range(len(distinct_list))}
# print(no_of_occurance)
# #
# print("Dictionary :- ",new_dict)
# for i in new_dict:
#     print(f" {i} : {new_dict[i]}")
# ==========================================================================================
# 2: Write a Python program that accepts number of subjects and then a list of subject names and a list marks.
# Print subject name and marks in order of its first occurrence comma seperated.
# Sample Input:
# Number of subjects: 3
# Input Subject name : Bengali
# Input Subject name : English
# Input Subject name : Math
# Input Subject marks : 23
# Input Subject name : 24
# Input Subject name : 45
# Sample output :
# Bengali--23 , English--24, Math--45
# =====================================SOLUTION======================================================
# rng=int(input("Enter how many subjects you want : "))
# sub_list = []
# marks_list= []
# for i in range(0,rng):
#     subject = input("Enter the subject : ")
#     sub_list.append(subject)
# print(sub_list)
# for i in range(0,rng):
#     marks = int(input(f"Enter the marks of subject {sub_list[i]} : "))
#     marks_list.append(marks)
# print(marks_list)
# my_dict ={sub_list[i]:marks_list[i] for i in range(len(sub_list))}
# print("Subject with marks are : ",my_dict)
# =======================================================================================================
# 3.Write a Python program to find the second lowest total marks of any student(s) from the given names and marks of each student using lists and lambda function. I
# Input number of students, names and grades of each student.
# Sample Input:
# Input number of students: 3
# Name: Avik Das
# Total marks: 89
# Name: ayan Roy
# Total marks: 75
# Name: Sayan Dutta
# Total marks: 93
# Sample Output:
# Names and Marks of all students:
# [['Avik Das ', 89.0], ['ayan Roy', 75.0], ['Sayan Dutta', 93.0]]
# Second lowest Marks: 89.0
# Names: Avik Das
# =====================================solution=================================================
# rng=int(input("Enter no of students"))
# stud_list = []
# marks_list= []
# for i in range(0,rng):
#     stud = input("Enter the Student name : ")
#     stud_list.append(stud)
# print(stud_list)
# for i in range(0,rng):
#     marks = int(input(f"Enter the marks of student {stud_list[i]}: "))
#     marks_list.append(marks)
# print(marks_list)
# my_dict = dict(zip(stud_list,marks_list))
# print("Subject with marks are : ",my_dict)
# dict_to_set = set(my_dict.values())
# dict_to_list = list(dict_to_set)
# dict_to_list.sort()
#
# second_lowest = dict_to_list[1]
# ind_of_2nd_low= marks_list.index(second_lowest)
# print("second_lowest Marks are : ", second_lowest)
# list_of_2nd_low = [i for i in my_dict if my_dict[i] == second_lowest]
# print("Name of Student: ",list_of_2nd_low)

# ===============================================================================================
# 4. Write a Python program to find the item with maximum frequency in a given list.
#
# Sample :
# Original list:
# [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 2, 4, 6, 9, 1, 2]
# Item with maximum frequency of the said list:
# (2, 5)

# my_list = [1,2,2,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,42]
# my_set = set(my_list)
# no_dups_list = list(my_set)
# no_of_occurence = []
# for i in my_set:
#     count =0
#     for j in my_list:
#         if i == j :
#             count+=1
#     no_of_occurence.append(count)
# print(my_list)
# print(my_set)
# print(no_dups_list)
# print(no_of_occurence)
# freq_dict = dict(zip(no_dups_list,no_of_occurence))
# max_freq = max(no_of_occurence)
# elements_with_highest_freq = [i for i in freq_dict if freq_dict[i] == max_freq]
# print(freq_dict)
# print(f"Elements {elements_with_highest_freq} is/are having highest frequency as : {max_freq}")
# print(f"Element {no_dups_list[no_of_occurence.index(max(no_of_occurence))]} has the highest frequency {max(no_of_occurence)}")
# -------------------------------------------------------------------------------------------------------------------------------------
#
# 5.Write a Python program to count most and least common characters in a given string.
#
# Sample :
# Original string:
# hello world
# Most common character of the said string: l
# Least common character of the said string: h
# =====================================solution=================================================
# str_1 =input("Enter the String : ")
# str_set = set(str_1)
# str_list = list(str_set)
# print(str_set)
# print(str_list)
# no_of_occur = []
# for i in str_list:
#     count = 0
#     for j in str_1:
#         if i == j:
#             count+=1
#     no_of_occur.append(count)
# print(no_of_occur)
# my_dict = dict(zip(str_list,no_of_occur))
# print(my_dict)
# max_occur = max(no_of_occur)
# min_occur = min(no_of_occur)
# list_of_max = [i for i in my_dict if my_dict[i] == max_occur]
# list_of_min = [i for i in my_dict if my_dict[i] == min_occur]
# print(f"""Most common character of the said string:" {list_of_max}"
#         \n Least common character of the said string: {list_of_min}""")
# ================================================================================
# ================================================================================
# 6. Write a Python program to count the occurrence of each element of a given list.
# Sample :
# Original List:
# ['Green', 'Red', 'Blue', 'Red', 'Orange', 'Black', 'Black', 'White', 'Orange']
# Count the occurrence of each element of the said list:
# Counter({'Red': 2, 'Orange': 2, 'Black': 2, 'Green': 1, 'Blue': 1, 'White': 1})
# Original List:
# [3, 5, 0, 3, 9, 5, 8, 0, 3, 8, 5, 8, 3, 5, 8, 1, 0, 2]
# Count the occurrence of each element of the said list:
# Counter({3: 4, 5: 4, 8: 4, 0: 3, 9: 1, 1: 1, 2: 1})
# =====================================solution=================================================
# my_list = []
# rng = int(input("How many elemenst your want to add: "))
# for i in range(0, rng):
#     ele = input("Enter the Element: ")
#     if ele.isdigit():
#         print("integer")
#         my_list.append(int(ele))
#     else:
#         print("String")
#         my_list.append(ele)
# print(my_list)
# word_distinct = set(my_list)
# distinct_list = list(word_distinct)
# print(distinct_list)
# count = 0
# no_of_occurance = []
# for i in distinct_list:
#     count = 0
#     for j in my_list:
#         if i == j:
#             count += 1
#     no_of_occurance.append(count)
# print(no_of_occurance)
# new_dict = dict(zip(distinct_list, no_of_occurance))
# print(new_dict)
# =========================================================================================

# 7.Write a program that calculates a user's BMI using the user's weight and height.
# BMI is calculated by dividing the person's weight in kg by the square of the person's height in meters. Round the result to a whole number.
# Sample :
# height = 1.85
# weight = 75
# Output: 22
import math

# =====================================solution=================================================
# print("welcome to BMI Calculation!!")
# h = float(input("Enter your Height (in meters):"))
# w = float(input("Enter your Weight "))
# bmi = int(round(w/(h**2),0))
# print("BMI is :", bmi)
# ==================================================================================================

# 8.Create a program that takes the user's current age as input and calculates how many days, weeks, and
# months they have left to live if they would get 99 years old.
# For this exercise, we assume that a year has 365 days, 52 weeks, and 12 months.We don't take leap years into account!
# Print the final result to the console using an f-String!
# Sample :
# Please enter your age today : 36
# Output :
# You have 22995 days, 3276 weeks, and 756 months left to live a joyful life !
# =====================================solution=================================================
# age = int(input("Enter your Age: "))
# left_age = 99 - age
# left_days = left_age * 365
# left_week = left_age * 52
# left_months = left_age * 12
# print(f"You have {left_days} days, {left_week} weeks, and {left_months} months left to live a joyful life !")
# =================================================================================================
#
# 9. Print a greeting to the screen, welcoming our user to the Tip Calculator.
# Ask the user how much the total bill is and store the value in a variable.
# Ask the user how much percent tip they want to give the waiter and store the value in a variable.
# Ask the user how many people they want to split the bill between and store the value in a variable.
# Calculate how much each of your friends has to pay if the bill, including tip, is equally spread among them.
# Round the result to two positions after the comma and print it to the console
# Sample1:
# When you input the following amounts:
# Total bill: 150
# Tip percentage: 12
# Split between people: 5
# The total amount paid by each person should be 33.60, not 33.6
# If the bill is 150 split between 5 people with a 12% tip,
# you can use this formula to calculate the final amount each person has to pay
# (feel free to use any other formula to get to the result!):  150/5 * 1.12
# Sample2 :
# If you enter the following values:
# Total bill: 180
# Tip percentage: 15
# Split between people: 4
# Output:
# Each person has to pay : 51.75
# =====================================solution=================================================
# bill = int(input("Enter your bill: "))
# tip_percent = int(input("Enter the tip percentage you want to offer: "))
# split_count = int(input("In how many people you want to split the total bill: "))
# total_bill = bill + (bill * (tip_percent / 100))
# per_head_bill = total_bill / split_count
# print(f"Total bill is {total_bill} Rupees. \nEach person has to pay {per_head_bill} rupees.")


# ===============================================================================================

# 10.create a class named "CDAC_course"
# class variable
# 	instructors_so_far_for_the_course[] // list
# instance variables
# 	subject_name (public)
# 	subject_instructor_name (public)
# 	subject_instructor_designation ( protected)
# 	subject_instructor_company ( protected)
# 	subject_instructor_feedback ( private)
# instance methods
#    get_subject_instructor_feedback()
# classmethod
#    get_instructors_so_far_for_the_course()
#    // append to the existing list in this func
#    set_instructors_so_far_for_the_course(instructor_name)
# create a function main that
# a) creates an obj of course class with values
#    DIOT-Python,Elon Musk,CEO at Tesla ,Cdac,"Sample Feedback"
# b) Add Elon musk to the class list variable instructors_so_far_for_the_course
# c) print Elon Musk feedback
# d) Print all the  instructors_so_far_for_the_course

# =====================================solution=================================================
# class CdacCourse:
#     instructors_so_far_for_the_course = []  # Class_variable (as a list)
#
#     def __init__(self, sub_name, instr_name, _instr_desig, _instr_company, __instr_feedback):
#         self.sub_name = sub_name
#         self.instr_name = instr_name
#         self._instr_desig = _instr_desig
#         self._instr_company = _instr_company
#         self.__instr_feedback = __instr_feedback  # All_are_Instance_Variable
#
#     def get_subject_instructor_feedback(self):
#         return self.__instr_feedback
#
#     @classmethod
#     def set_instructors_so_far_for_the_course(self,instructor_name):
#         self.instructors_so_far_for_the_course.append(instructor_name)
#
#     @classmethod
#     def get_instructors_so_far_for_the_course(self):
#         return self.instructors_so_far_for_the_course
# c1 = CdacCourse("DIOT-Python", "Elon Musk", "CEO at Tesla", "Cdac", "Sample Feedback")
# #c2 = CdacCourse("DBMS", "GR", "TL", "Oracle", "Good!")
# print(c1.get_subject_instructor_feedback())   #Calling Instance Method
# CdacCourse.set_instructors_so_far_for_the_course(c1.instr_name) #Adding Elon musk to the cls var instructors_so_far_for_the_course
# #c2.set_instructors_so_far_for_the_course(c2.instr_name)
# print(CdacCourse.get_instructors_so_far_for_the_course())  #Calling ClassMethod
# ===============================================================================================
# 11. Write exception handling for below code's invocation block
# import time
# conclude = "And what leads you to that conclusion?"
# district = "Finest in the district, sir."
# cheese = "It's certainly uncontaminated by cheese."
# clean = "Well, it's so clean."
# shop = "Not much of a cheese shop really, is it?"
# cust = "Customer: "
# clerk = "Shopkeeper: "
# def fun(reaper):
#     if reaper == 'spam':
#         print('spam')
#     elif reaper == 'cheese':
#         print()
#         print('Spam, Spam, Spam, Spam, Beautiful Spam')
#     elif reaper == 'mr death':
#         print()
#         return('{}{}\n{}{}'.format(cust, shop, clerk, district))
# def more_fun(language):
#     if language == 'java':
#         test = [1, 2, 3]
#         test[5] = language
#     elif language == 'c':
#         print('{}{}\n{}{}'.format(cust, conclude, clerk, clean))
# def last_fun():
#     print(cust, cheese)
#     time.sleep(1)
#     import antigravity
# # invocation code below where you need to do try,except block and
# # make sure you program does not throw an exception
# # rather prints with a message to the user on what went wrong and ask him to retry atleast once
# first_try = ['spam', 'cheese', 'mr death']
# joke = fun(first_try[0])
# not_joke = fun(first_try[2])
# langs = ['java', 'c', 'python']
# more_joke = more_fun(langs[0])
# ===============================================================================================

# ===============================================================================================

# 12. Write a program to find the count of "triple" value in a string.
# A "triple" in a string is a sequence of characters appearing thrice times in a row.
# Return the count of triples in the given string. The triples may overlap
# Sample:
# triple_counter("defXXXdef") returns 1
# triple_counter("zzzabxxxxcd") returns 3 since xxx and xxx is present but in overlapping state
# triple_counter("f") → 0
# =====================================solution=================================================
# def triple_counter(string):
#     itr = 0
#     count= 0
#     while itr < len(string) -2:
#         if string[itr] == string[itr+1] == string[itr+2]:
#             count+=1
#         itr+=1
#     return count
# print("triple count is : ",triple_counter("fffsdcadddd"))
# ===============================================================================================
# ===============================================================================================
# 13. Given a string and a non-negative int n, return a string ouput that is n copies of the original string.
# string_multiplier('Hi', 2) → 'HiHi'
# string_multiplier('Hi', 3) → 'HiHiHi'
# string_multiplier('Hi', 1) → 'Hi'
# =====================================solution=================================================
# def string_multiplier(string, mul_factor):
#     new_str = (string)*mul_factor
#     return new_str
#
# print(string_multiplier(input("Enter the string: "), int(input("Enter the multiplication factor: "))))
# ===============================================================================================
# 14. Below we've provided a list of tuples, where each tuple contains details about an employee of a shop.
# Print how much each employee is due to be paid at the end of the week in a nice, readable format.
# employees = [
#     ("Rolf Smith", 35, 8.75),
#     ("Anne Pun", 30, 12.50),
#     ("Charlie Lee", 50, 15.50),
#     ("Bob Smith", 20, 7.00)
# ]

# ===============================================================================================
# 15. Write a function in Python to read lines from a text file "notes.txt". Your function should find and display the occurrence of the word "the".
# Note :
# Create a file "notes.txt" with the following content below:
# "India is the fastest-growing economy. India is looking for more investments around the globe. The whole world is looking at India as a great market. "
# "Most of the Indians can foresee the heights that India is capable of reaching."
# The output should be 5
f = open("notes.txt", "r")
all_in_one = f.read()
print(all_in_one)
split_content =[]
split_content = all_in_one.split(" ")
word= "the".lower()
count = 0
for i in split_content:
    if i.lower() == word:
        count+=1
print(split_content)
print(f"Count of word:- \"{word}\" is: {count}")