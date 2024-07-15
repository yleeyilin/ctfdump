import gmpy2
import binascii
import sympy

e = 65537
n = 13118792276839518668140934709605545144220967849048660605948916761813
ct = 8124539402402728939748410245171419973083725701687225219471449051618

def decrypt_flag(p, q, c):
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = 65537
    d = gmpy2.invert(e, phi_n)
    decrypted_flag = pow(c, d, n)
    return decrypted_flag

# for p in sympy.primerange(2**56, 2**112):
#     if (n % p == 0):
#         q = n / p
#         print(f"p: {p}")
#         print(f"q: {q}")

# using factordb
n1 = 3058290486427196148217508840815579
n2 = 4289583456856434512648292419762447
print(n1 * n2)
print(n)

decrypted_value = decrypt_flag(n1, n2, ct)

hex_value = hex(decrypted_value)[2:]
plaintext = binascii.unhexlify(hex_value).decode()

print(f"Decrypted Hex: {hex_value}")
print(f"Decrypted Plaintext: {plaintext}")