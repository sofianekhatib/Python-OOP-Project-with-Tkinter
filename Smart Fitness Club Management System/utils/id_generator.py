import random
class IDGENERATOR:
    @staticmethod
    def GenerateProgramId():
        return f"PRO{random.randint(100 , 999)}"
    