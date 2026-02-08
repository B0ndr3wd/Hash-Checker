import re

def check_MD5(hash):
    '''Check if ur hash is MD5'''
    x = re.findall(r'[a-fA-F0-9]{32}', hash)
    if x:
        return True
    
# Test Function
assert check_MD5("5d41402abc4b2a76b9719d911017c592") == True
assert not check_MD5("5d41402abc4b2a76b9719d911017c")
assert not check_MD5("5d41402abc4b2a76b9719d911017c***")