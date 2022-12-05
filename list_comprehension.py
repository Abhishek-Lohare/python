#Removing Duplicates from the string and returning a unique chars string.
my_str = "AAbbbaaaBBBccclkjjqedu"
print("Original List: ", my_str)
unique_list = []
#concept of list comprehension
[unique_list.append(i) for i in list(my_str) if i not in unique_list]
#Syantax for list Comprehension---->   [Expression for iterator in iterable condition]
str1 = ''
for elem in unique_list:
    str1+=elem
print("Unique char list: ",str1)
############################################################################################################
# Using list comprehension print the words of string in uppercase
List = [chars.upper() for chars in 'I\'m the groot'.split(" ")]
print(List)

#Find all of the numbers from 1–1000 that are divisible by 8
List = [i for i in range(1,1001) if i%8 == 0]
print(List)

#Find all of the numbers from 1–1000 that have a 6 in them
List = [i for i in list(range(1, 1001)) if "6" in str(i)]             #*****TRICKY*****#
print(List)

#Count the number of spaces in a string (use string above)
List = [i for i in "Practice Problems to Drill List Comprehension in Your Head" if i == " "]
print(len(List))

# Remove all of the vowels in a string (use string above)
finalstr = ''
output_list = [i for i in "This is my String of combination AAAEEIIOOUU".lower() if i not in ['a', 'e', 'i', 'o', 'u']]
for i in output_list:
    finalstr += i
print(finalstr)

# # Use a dictionary comprehension to count the length of each word in a sentence (use string above)
my_str = "This is my String of combination AAAEEIIOOUU"
# #using general list comprehensions
len_count = dict(zip([j for j in my_str.split()],[len(i) for i in my_str.split()]))
print(len_count)
#using Dict comprehensions
dict_str = {x: len(x) for x in my_str.split()}
print(dict_str)


#Find all of the words in a string that are less than 5 letters (use string above)
cnt_gt_than_5 = [i for i in my_str.split() if len(i)>5]
print(cnt_gt_than_5)


#Use a nested list comprehension to find all of the numbers from 1–1000 that are divisible by any single digit besides 1(2-9)
num_list = {i for i in range(1,1001) for j in range(2,10) if i%j == 0}
print(num_list)
# print(num_list)

