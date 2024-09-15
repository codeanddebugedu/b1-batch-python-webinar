def interview(lst, tot):
    if len(lst) != 8:
        return "disqualified"
    elif sum(lst) + 20 > 120:
        return "disqualified"
    elif tot > 120:
        return "disqualified"
    else:
        return "qualified"
