from person import Person
class Member(Person):
    def __init__(self , id , first_name , last_name , phone , weight , height , goal):
        super().__init__(id , first_name , last_name , phone)
        self.__weight = weight
        self.__height = height
        self.__goal = goal
    
    def getWeight(self):
        return self.__weight
    def getHeight(self):
        return self.__height
    def getGoal(self):
        return self.__goal
    
    def setWeight(self , weight):
        self.__weight = weight
    def setHeight(self , height):
        self.__height = height
    def setGoal(self , goal):
        self.__goal = goal


    def __str__(self):
        return super().__str__() + f" - Weight : {self.getWeight()} - Height : {self.getHeight()} - Goal : {self.getGoal()}"
        
