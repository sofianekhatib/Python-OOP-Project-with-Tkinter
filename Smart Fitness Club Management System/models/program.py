from utils.validator import Validator
from utils.id_generator import IDGENERATOR
import random
class Program:
    def __init__(self , program_goal , difficulty):
        program_id = IDGENERATOR.GenerateProgramId()
        self.setProgramId(program_id)
        self.__program_goal = program_goal
        self.__difficulty = difficulty
        self.assigned_members = []
    validator = Validator()
    def getProgramId(self):
        return self.__program_id
    def getProgramGoal(self):
        return self.__program_goal
    def getDifficulty(self):
        return self.__difficulty
    
    def setProgramId(self , program_id):
        self.validator.validateProgramId(program_id)
        self.__program_id = program_id
    def setProgramGoal(self , program_goal):
        self.__program_goal = program_goal
    def setDifficulty(self , difficulty):
        self.__difficulty = difficulty
    
    def __str__(self):
        return f" Program id : {self.getProgramId()} - Program goal : {self.getProgramGoal()} - Diffictlly : {self.getDifficulty()}"

goals = ["Bulking", "Cutting", "Strength", "Fitness"]
levels = ["Beginner", "Intermediate", "Advanced"]

programs = []

for _ in range(10):
    goalschoice = random.choice(goals)
    levelschoice = random.choice(levels)
    p = Program(goalschoice , levelschoice)
    programs.append(p)


for program in programs:
        print(program)

    

    

    

        