from Cryptodome.Util.number import getPrime, bytes_to_long, long_to_bytes

flag = bytes_to_long(b"REDACTED")
p = getPrime(512)
q = getPrime(512)
n = p*q # (also be almost prime w prime factors) 
e = 3

ciphertext = pow(flag, e, n)

# (flag ^ 3) % n = ciphertext

print("n: ", n)
print("e: ", e)
print("ciphertext: ", ciphertext)
print(pow(flag, e))