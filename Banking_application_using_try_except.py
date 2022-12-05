# try:
#     a= int(input())
#     b= int(input())
#     c = a/b
#     print(c)
# except ZeroDivisionError:
#     print("denominator is 0")
#
# print("Further part is being executed!!!")
# =========================================================
class InsufficientBalanceError(Exception):
    def __init__(self, accno,
                 cb):  # get called automatically when we are raising the exception with an instantiated object.
        self.__accno = accno
        self.__curbal = cb

    def get_details(self):
        return {'Acc no': self.__accno, 'Current Balance': self.__curbal}


class Customer:
    def __init__(self):
        self.__dct = {}

    def append(self, accno, n, bal):
        self.__dct[accno] = {'Name': n, 'Balance': bal}
        # here we have created a dictionary with values as another dictionary.

    def display(self):
        for k, v in self.__dct.items():
            # two iterator are used one for iterrating on the acc_no and other for its internal dict.value which is itself a dictionary
            print(k, v)
        print()

    def deposit(self, accno, amt):
        d = self.__dct[accno]
        d['Balance'] = d['Balance'] + amt
        self.__dct[accno] = d
    def afterwithdraw(self, accno):
        x = self.__dct[accno]
        return x
    def withdraw(self, accno, amt):
        d = self.__dct[accno]  # here in d we are storing the values(values of dictionaries with keys:- Name & Balance)
        curbal = d['Balance']
        if curbal - amt > 5000:
            d['Balance'] = d[
                               'Balance'] - amt  # here we are accessing the value of internal dict with key as 'name' and we have updated its value.
            self.__dct[accno] = d
            print("Updated balance of Ram:", d['Balance'])
        else:
            raise InsufficientBalanceError(accno,
                                           curbal)  # here we have instantiated object with instance variable accno & curbal


c = Customer()
c.append(123, 'Ram', 9000)
c.append(124, 'Sham', 8000)
print(c)
c.display()
c.deposit(123, 1000)
c.deposit(124, 2000)
c.display()
try:

    c.withdraw(123, 9000)
    print("amount withdrawal successfully!!!!")
    print("After withdrawal Balance Details ",c.afterwithdraw(123))
except InsufficientBalanceError as insfb:
    print('!!Insuffient Balance, Money cant be withdraw!!')
    print(insfb.get_details())
