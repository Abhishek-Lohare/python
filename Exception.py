class Customer:
    def __init__(self):
            self.__dict={}

    def append(self,accno,n,bal):
            self.__dict[accno]={'Name':n,'Balance':bal}

c = Customer()
c.append(123,'Sumeet',9000)
print(c)

