import os
import sys
import python_include

python_include.file("../other_nested/include_me.py", globals())

def hello():
    print('this should be ..."nested/include_me.py" ', __file__)
    print('hello')