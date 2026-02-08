import re
def check_SHA1(hash):
    '''Check if ur hash is SHA1'''
    x = re.findall(r'[a-fA-F0-9]{40}', hash)
    if x:
        return True
    
# Test the function
assert check_SHA1("aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d") == True
assert not check_SHA1("5d41402abc4b2a76b9719d911017c592")