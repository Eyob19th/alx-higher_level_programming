#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    newdic = list(a_dictionary.items())
    newdic.sort(key=lambda item: item[1])
    return (newdic[-1][0])
