class Student:
    # def __init__(self) -> None:
    #     self.id = int(input("Enter ID = "))
    #     self.name = input("Enter name = ")
    #     self.age = int(input("Enter age = "))
    #     self.gender = input("Enter gender = ")
    #     self.city = input("Enter city = ")

    def __init__(self, id, name, age=18, gender="", city="Surat") -> None:
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.city = city

    # Methods
    def display(self):
        print(f"ID = {self.id}")
        print(f"Name = {self.name}")
        print(f"Age = {self.age}")
        print(f"Gender = {self.gender}")
        print(f"City = {self.city}")

    def update(self, new_name=None, new_age=None, new_gender=None):
        if new_name != None:
            self.name = new_name
        if new_age != None:
            self.age = new_age
        if new_gender != None:
            self.gender = new_gender


s1 = Student(1, "Anirudh")
s1.display()
s1.update(new_name="XYZ", new_gender="Male")
s1.display()
