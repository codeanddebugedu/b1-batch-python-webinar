def highest_scorer(students_scores):
    highest_score = -float("inf")
    highest_scorer_name = ""
    for name, score in students_scores.items():
        if score > highest_score:
            highest_score = score
            highest_scorer_name = name
    return highest_scorer_name


# Alternate Way
# def highest_scorer(students_scores: dict[str, int]):
#     highest_score = max(students_scores.values())
#     for name, score in students_scores.items():
#         if score == highest_score:
#             return name


print(highest_scorer({"Alice": 95, "Bob": 87, "Charlie": 95, "David": 78, "Eva": 90}))
print(highest_scorer({"Frank": 82, "Grace": 91, "Hannah": 88, "Ian": 91, "Jack": 76}))
print(highest_scorer({"Liam": 85, "Mia": 92, "Noah": 78, "Olivia": 89, "Sophia": 95}))
