"""
Write a function called once.
This function accepts a function and returns a new function that can only be invoked once.
If the function is invoked more than once, it should return None.
Hint you will need to define a new function inside your once function and return that function.
You can add properties to your inner function to see if it has run already.
def add(a,b):
    return a+b

oneAddition = once(add)

oneAddition(2,2) # 4
oneAddition(2,2) # None
oneAddition(12,200) # None
"""


def once(fn):
    fn.is_called = False

    def inner(*args):
        if not fn.is_called:
            fn.is_called = True
            return fn(*args)

    return inner
