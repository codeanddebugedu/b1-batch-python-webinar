def wash_hands(N, nM):
    secs_per_day = 21 * N
    secs_per_month = secs_per_day * 30
    total_secs = secs_per_month * nM
    total_mins = total_secs / 60
    remainder_secs = total_secs % 60
    return f"{int(total_mins)} and {remainder_secs} seconds"
