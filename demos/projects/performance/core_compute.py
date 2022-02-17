import functools
import math
import time


def compute_analytics(search, rows):
    search_data = read_data(search)
    db_data = read_data(rows)

    return learn(search_data, db_data)


def read_data(data):
    for _ in range(len(data)):
        # Imagine: We switch to NumPy, gain 20x
        # time.sleep(.02)
        time.sleep(.001)

    return data


def learn(search_data, db_data):
    total = 0
    for ids, s in enumerate(search_data):
        for idd, d in enumerate(db_data):
            for r in range(1, 100):
                val1 = ids * idd * len(s)
                # val2 = math.pow(idd, 7)
                val2 = compute_pow(idd, 7)

                res = math.sqrt(val1 * val1 + val2 * val2)
                # mod = math.pow(-1, ids + r)
                mod = compute_pow(-1, ids + r)

                total += res * mod
                total = total

    return total


@functools.lru_cache()
def compute_pow(x, y):
    return math.pow(x, y)
