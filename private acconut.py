class account:
    def __init__(self,name,password):
        self.name=name
        self.__password=password
    def reset(self):
        print(self.__password)    
a1=account("ankit","abcd")
# print(a1.name,a1.__password)
print(a1.reset())

