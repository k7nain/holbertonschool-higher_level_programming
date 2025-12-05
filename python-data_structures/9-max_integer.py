#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    max1 = my_list[0]
    for i in my_list[1:]:
        if i > max1:
            max1 = i
    return max1
