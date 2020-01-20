# # ----------- SUM OF DIGITS--------------------

from time import time
def sum1(number):
    s = 0
    while number:
        s , number = s+number%10 , number // 10
    return s


def sumall(number):
    s = 0
    while number: s , number = s+number%10 , number // 10
    if s > 10: return sumall(s)
    return s

# # ------------- OR----------------
'''
def digital_root(n):
    x = sum(int(digit) for digit in str(n))
    if x < 10:
        return x
    else:
        return digital_root(x)

 '''    
 #-----------use => x = sum(map(int, str(number)))
def digital_root(n):
    x = sum(int(digit) for digit in str(n))
    if x < 10: return x
    return digital_root(x)


number = 1234567890232938923728937289738324423748238482334789237489723894788923748726784682347623462374627365476235762357465237647236323862837682736872638728376287368276823647823647625374672354716523476523746578236546712
# s = time()
# print(sum1(number) , (time() - s)*10**9)

# s1 = time()
# print(sum(map(int, str(number))) , (time() - s1)*10**9)

print(sumall(number) )