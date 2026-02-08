from Check_MD5 import *
from Check_SHA1 import *
from Check_SHA256 import *

def hash_check():
    '''MD5 / SHA1 / SHA256'''
    if check_MD5():
        print("Its MD5 !")
    elif check_SHA1():
        print("Its SHA1 !")
    elif check_SHA256():
        print("Its SHA256 !")
    else:
        print("Its not MD5 or SHA1 or SHA256 :( ")