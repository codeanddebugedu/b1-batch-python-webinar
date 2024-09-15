def majority_vote(lst):
    frequency = {}
    for vote in lst:
        if vote in frequency:
            frequency[vote] += 1
        else:
            frequency[vote] = 1

    n = len(lst)
    for name, vote in frequency.items():
        if vote > n // 2:
            return name
    return None
