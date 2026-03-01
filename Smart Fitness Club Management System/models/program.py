class Program:
    def __init__(self , program_id , program_goal , difficulty , assigned_members):
        self.__program_id = program_id
        self.__program_goal = program_goal
        self.__difficulty = difficulty
        self.assigned_members = []

    def getProgramId(self):
        return self.__program_id
    def getProgramGoal(self):
        return self.__program_goal
    def getDifficulty(self):
        return self.__difficulty
    
    def setProgramId(self , program_id):
        self.__program_id = program_id
    def setProgramGoal(self , program_goal):
        self.__program_goal = program_goal
    def setDifficulty(self , difficulty):
        self.__difficulty = difficulty
    
    def __str__(self):
        return f" Program id : {self.getProgramId()} - Program goal : {self.getProgramGoal()} - Diffictlly : {self.getDifficulty()}"


    

    

        