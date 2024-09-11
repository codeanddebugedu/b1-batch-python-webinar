"""
Required vs Default Parameters
"""


def calculate_marks(physics=0, chemistry=0, science=0, english=0, computer=0):
    print(f"physics = {physics}")
    print(f"chemistry = {chemistry}")
    print(f"science = {science}")
    print(f"english = {english}")
    print(f"computer = {computer}")
    total = physics + chemistry + science + english + computer
    percentage = total / 5
    print(f"Total {total} and percentage = {percentage}")


calculate_marks()
