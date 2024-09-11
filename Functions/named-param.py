"""
Named Parameters
"""


def calculate_marks(physics, chemistry, science, english, computer):
    print(f"physics = {physics}")
    print(f"chemistry = {chemistry}")
    print(f"science = {science}")
    print(f"english = {english}")
    print(f"computer = {computer}")
    total = physics + chemistry + science + english + computer
    percentage = total / 5
    print(f"Total {total} and percentage = {percentage}")


calculate_marks(10, 20, computer=44, english=100, science=87)
calculate_marks(english=55, computer=32, chemistry=11, physics=34, science=100)
