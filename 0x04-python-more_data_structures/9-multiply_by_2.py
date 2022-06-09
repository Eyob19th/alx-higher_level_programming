#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newdic = dict(a_dictionary)
    for x in newdic:
        newdic[x] *= 2
    return newdic
