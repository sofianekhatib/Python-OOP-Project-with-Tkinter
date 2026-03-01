class Person:
    def __init__(self , id , first_name , last_name , phone):
        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._phone = phone

    def getId(self):
        return self._id
    def getFirstName(self):
        return self._first_name
    def getLastName(self):
        return self._last_name
    def getPhone(self):
        return self._phone
    
    def setId(self , id):
        self._id = id 
    def setFirstName(self , first_name):
        self._first_name = first_name
    def setLastName(self, last_name):
        self._last_name = last_name
    def setPhone(self , phone):
        self._phone = phone
    
    def __str__(self):
        return f"{self.getFirstName()} {self.getLastName()} [{self.getId()}] : Phone :  {self.getPhone()}"



        