from Check_MD5 import *
from Check_SHA1 import *
from Check_SHA256 import *

def hash_check():
    '''MD5 / SHA1 / SHA256'''
    i = 0
    while True:
        hash = input("Copy and Paste ur hash here -->  ")

        if check_MD5(hash):
            print("Its MD5 !")
        elif check_SHA1(hash):
            print("Its SHA1 !")
        elif check_SHA256(hash):
            print("Its SHA256 !")
        else:
            print("Its not MD5 or SHA1 or SHA256 :( ")
        
        end = input("Do u want test another hash ? yes // no : ")
        if end != 'yes':
            break
      
# Call the function
hash_check()