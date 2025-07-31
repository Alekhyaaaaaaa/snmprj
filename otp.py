# import random

# def generate_custom_otp():
#     uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     lowercase = "abcdefghijklmnopqrstuvwxyz"
#     digits = "0123456789"

#     otp = (
#         random.choice(uppercase) +   # Capital letter
#         random.choice(lowercase) +   # Small letter
#         str(random.randint(0, 9)) +   # Digit
#         random.choice(uppercase) +   # Capital letter
#         random.choice(lowercase) +   # Small letter
#         str(random.randint(0, 9))     # Digit
#     )
#     return otp
# print(generate_custom_otp())

import random
def genotp():
    otp=''
    ul=[chr(i) for i in range(ord('A'),ord('Z')+1)]
    sl=[chr(i) for i in range(ord('a'),ord('z')+1)]
    for i in range(2):
        otp=otp+random.choice(ul)  #otp=''+A=A
        otp=otp+random.choice(sl)  #otp='A'+'k'='Ak'
        otp=otp+str(random.randint(0,9)) #otp='Ak'+'9'='Ak9'
    return otp

