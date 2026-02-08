import re

def check_SHA256(hash):
    '''Check if ur hash is SHA256'''
    x = re.findall(r'[a-fA-F0-9]{64}', hash)
    if x :
        return True
    
# Test function
assert check_SHA256("2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824") == True
assert not check_SHA256("2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e730433629")