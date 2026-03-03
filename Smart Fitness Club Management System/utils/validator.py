import re
from .id_generator import IDGENERATOR
class Validator:
    def __init__(self):
        self.ids_in_use = set()
        self.program_ids_in_use = set()

    def ValidateId(self , id_value , role):

        if id_value in self.ids_in_use:
            raise ValueError("ID must be unique")
        
        if not id_value:
            raise ValueError("Please fill in the ID")
        
        patterns = {
            "member": r"^MEM\d{3}$",
            "coach": r"^COA\d{3}$"
        }

        if not role in patterns:
            raise ValueError("Invalid role type")
        
        if not re.fullmatch(patterns[role] , id_value):
            raise ValueError(f"Please respect the {role} id format")
        
        self.ids_in_use.add(id_value)
        
    def ValidateFirstName(self , first_name):
        if len(first_name) <= 2:
            raise ValueError("The first name should have 2 characters for minimum")
        
        pattern = r"^[A-Za-z]{2,}$"

        if not re.fullmatch(pattern , first_name):
            raise ValueError("The First name should not have any digits or special characters")
        
    def ValidateLastName(self , last_name):
        if len(last_name) <= 2:
            raise ValueError("The last name should have 2 characters for minimum")
        
        pattern = r"^[A-Za-z]{2,}$"

        if not re.fullmatch(pattern , last_name):
            raise ValueError("The last name should not have any digits or special characters")

    def ValidatePhone(self , phone):
        pattern = r"^(06|07)\d{8}$"
        if not re.fullmatch(pattern , phone):
            raise ValueError("The number should be Moroccan format")

    def validateWeight(self , weight):
        try:
            weight = float(weight)
        except ValueError:
            raise ValueError("The weight must be numeric")
        
        if weight < 30 or weight > 200:
            raise ValueError("Please the weight nust be between 30 and 200 kg")

    def validateHeight(self , height):
        try:
            height = float(height)
        except ValueError:
            raise ValueError("The height must be numeric")
        
        if height < 100 or height > 220:
            raise ValueError("Please the height nust be between 100 and 220 cm")
 
    def validateGoal(self , goal):
        AllowedValues = {"Bulking" , "Cutting" , "Strength"}
        if goal not in AllowedValues:
            raise ValueError("Please choose Bulking , Cutting or Strength")

    def validateSpecialization(self , spec):
        pattern = r"^[A-Za-z]{3,}$"
        if not re.fullmatch(pattern , spec):
            raise ValueError("Specialization must contains letters only and 3 characters for minimum")
        
    def validateYears(self , years):
        try :
            years = int(years)
        except ValueError:
            raise ValueError("Years must be numeric")
        if years > 50:
            raise ValueError("Cannot exceed 50")
        
    def validateProgramId(self , program_id):
        if program_id in self.program_ids_in_use:
            raise ValueError("The program id must be unique")
        self.program_ids_in_use.add(program_id)
        
