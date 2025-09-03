# define the parent class
class student:
    def __init__(self, name, department, Sex, Age):
        self.name = name
        self.department = department
        self.Sex = Sex
        self.Age = Age
# Lets define a scienc class        
class scienceStud(student):
    def __init__(self, Chemistry, Physis, name, department, Sex, Age):
        super().__init__(name, department, Sex, Age)
        self.Chemistry = Chemistry
        self.Physis = Physis
    def show_class():
        print(F"My name is {name} and I am a {} student")
        
# Lets define another clas called Art        
class ArtStudent(student):
    def __init__(self, Government, Art, name, department, Sex, Age):
        super().__init__(name, department, Sex, Age)
        self.Government = Government
        self.Art = Art

    def show_class():
        print(F"My name is {name} and I am a {} student")     

# Lets define a Commercial class        
class comercialStud(student):
    def __init__(self, Commerce, Accounting, name, department, Sex, Age)
        super().__init__(name, department, Sex, Age)
        self.Commerce = Commerce
        self.Accounting = Accounting

    def show_class():
        print(F"My name is {self.name} and I am a {self.department} student")