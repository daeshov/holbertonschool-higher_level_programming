#!/usr/bin/python3
def no_c(my_string):
    copy_str = [X for x in my_string if x != 'c' or X != 'C']
    return ("".join(copy_str))
