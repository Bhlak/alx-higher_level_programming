#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary or len(a_dictionary) == 0:
        return None

    kok = list(a_dictionary)[0]
    val = a_dictionary[kok]

    for k, v in a_dictionary.items():
        if v > val:
            val = v
            kok = k
    return kok
