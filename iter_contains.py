class Teams:
    def __init__(self, members):
        self.__members = members
        self.__index =-1
        
    def __len__(self):
        return len(self.__members)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.__index += 1
        if self.__index == len(self.__members):
            raise StopIteration
        return self.__members[self.__index]
       
    def __contains__(self, value):
        return value in self.__members
        

def main():
    classmates = Teams(['John', 'Steve', 'Tim'])
    print (len(classmates))
 
    for i in classmates:
        print (i)

    print ('Tim' in classmates)
    print ('Sam' in classmates)
        
main()