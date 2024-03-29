"""
Implement a function is_all_strings  that accepts a single iterable and
returns True if it contains ONLY strings.
Otherwise, it should return false.
is_all_strings(['a', 'b', 'c'])  #True
is_all_strings([2,'a', 'b', 'c'])  #False
is_all_strings(('hello', 'goodbye'))  #True
"""

def is_all_strings(l):
    return all(type(x) == str for x in l)
