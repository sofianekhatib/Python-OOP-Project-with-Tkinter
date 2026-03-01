from person import Person
class Coach(Person):
    def __init__(self, id, first_name, last_name, phone , specialization , years_experience):
        super().__init__(id, first_name, last_name, phone)
        self.__specialization = specialization
        self.__years_experience = years_experience
        self.__members_list = []
    
    def getSpecialization(self):
        return self.__specialization
    def getYears_experience(self):
        return self.__years_experience
    
    def setSpecialization(self , specialization):
        self.__specialization = specialization
    def setYears_experience(self , years_experience):
        self.__years_experience = years_experience
    

    def __str__(self):
        return super().__str__() + f"- Specialization : {self.getSpecialization()} - Years of experience : {self.getYears_experience()}"


