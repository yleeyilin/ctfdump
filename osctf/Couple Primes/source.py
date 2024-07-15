from Crypto.Util.number import *
from sympy import nextprime
import gmpy2

flag = b'REDACTED'

p = getPrime(1024)
q = nextprime(p) # returns the next prime after p
e = 65537

n = p * q
c = pow(bytes_to_long(flag), e, n) #flag ^ 65537 % (p*q)

print(f"c = {c}")
print(f"n = {n}")
print(f"test = {gmpy2.sqrt(n) ** 2}")