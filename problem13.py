"""
This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""

def is_char(code):
    return 1 if code <27 and code>0 else 0


def count(message):
    m=int(message)
    c = 1
    if len(message)==2:
        c= 1 + is_char(m)
    else : 
        c = is_char(int(message[:2]))+ count(message[1:])
        
    return c
print(count('1134'))