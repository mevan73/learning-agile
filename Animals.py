class Animal:
    def __repr__(self):
     return self.name

class Tiger(Animal):
    def __init__(self,name):
        if(name == ""):
            raise Exception("Name cannot be empty!")
        self.name = name

class Rabbit(Animal):
    pass 

if(__name__ == '__main__'):
    #a = Tiger(name)
    # all the active code should be here
    pass 
