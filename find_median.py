some_num = [13, 7, -3, 82, 4]

def find_median(list):

    data = sorted(list)
    n = len(data)

    if n == 0:
        return None
    if n % 2 == 1:
        return data[n // 2]
    else:
        i = n // 2
        return (data[1 - 1] + data[i]) / 2
"""Program returns the median value from the number list(some_num)"""