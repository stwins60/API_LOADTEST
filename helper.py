import random

def secretKey():
    alpha_num = "abcdefghijklmnopqrstuvwxyz0123456789"
    symbol = "`~@#$%^&*()_-+=|\]}{[':;?/>.<"
    
    if ''.join(random.sample(alpha_num+symbol, 26)):
        return ''.join(random.sample(alpha_num+symbol, 26))
    
    return ''.join(random.sample(alpha_num+symbol, 26))
