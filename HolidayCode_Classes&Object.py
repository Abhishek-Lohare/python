# Practice Problems: Classes and Objects (Chapters 5 and 6)
# 1) The class called Holiday is started below. An object of class Holiday represents a
# holiday during the year. This class has three instance variables:
# ● name, which is a String representing the name of the holiday
# ● day, which is an int representing the day of the month of the holiday ●
# month, which is a String representing the month the holiday is in
# a) Write a constructor for the class Holiday, which takes a String representing the
# name, an int representing the day, and a String representing the month as its arguments,
# and sets the class variables to these value
# b) Write a method inSameMonth, which compares two instances of the class Holiday,
# and returns the Boolean value true if they have the same month, and false if they do not.
# c) Write a method avgDate which takes an array of base type Holiday as its
# argument, and returns a double that is the average of the day variables in the Holiday
# instances in the array. You may assume that the array is full (i.e. does not have any null
# entries).
# d) Write a piece of code that creates a Holiday instance with the name “Independence
# Day”, with the day “4”, and with the month “July”.

#####################################################################################################
class Holiday:
    name_list = []
    day_list = []
    month_list = []

    def __init__(self, name, day, month):
        self.name = name
        self.day = day
        self.month = month
        Holiday.name_list.append(name)
        Holiday.day_list.append(day)
        Holiday.month_list.append(month)


    def inSameMonth(self, obj2):
        print(self.month,obj2.month)
        if self.month == obj2.month:
            return True
        else:
            return False

    # def set_class_variable(self):
    #     Holiday.name_list.append(self.name)
    #     Holiday.day_list.append(self.day)
    #     Holiday.month_list.append(self.month)

    def get_class_variable(self):
        return "Holiday's name",Holiday.name_list, "Months:",Holiday.month_list, "Days: ",Holiday.day_list

    @staticmethod
    def avgDate():
        return "Average of Date :",sum(Holiday.day_list)/len(Holiday.day_list)

#QUE1:-
h1 = Holiday("ABC", 10, "August")
h2 = Holiday("XYZ", 20, "June")
#h1.set_class_variable()
print(h1.get_class_variable())
#h2.set_class_variable()
print(h2.get_class_variable())

#QUE2:-
print(h1.inSameMonth(h2))

#QUE3:-
print(Holiday.avgDate())

#QUE4:-
h3 = Holiday("Independence Day",4,"July")
#h3.set_class_variable()