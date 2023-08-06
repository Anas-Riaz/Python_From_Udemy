class student :
    def __init__(self, arg_name, arg_section, arg_Roll_Number):
        self.name = arg_name
        self.section = arg_section
        self.roll_number = arg_Roll_Number
    
    
    def printdetails(self):
        return f"Name :{self.name} , Section : {self.section} , Roll number : {self.RollNumber} ."

anas = student("Anas" ,"B" , "B-20102156")
arqam = student("Arqam" , "B" ,"B-20102156")

# anas.name = "Anas"
# anas.section = "B" 
# anas.RollNumber = "B-20102156"

# arqam.name = "Muhammad Arqam Aftab"
# arqam.section = "B" 
# arqam.RollNumber = "B-20102080"

print("="*50)

print(anas.name)

print("="*50)

print(anas.printdetails())