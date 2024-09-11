"""
Args and Kwargs
"""


def display(name, age, *marks):
    print(f"Name = {name}")
    print(f"Age = {age}")
    print(f"Marks ={sum(marks)}")


display("Anirudh", 18, 1, 2, 2)
display("Sanjay", 66, 65, 43, 67, 98, 65)
display("Nihar", 66, 65)
