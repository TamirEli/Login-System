import random


def is_prime(number):
    """Check if a number is prime."""
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def gcd(a, b):
    """Calculate the greatest common divisor of two numbers."""
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Calculate the least common multiple of two numbers."""
    return abs(a * b) // gcd(a, b)


def modinv(a, m):
    """
    Calculate the modular multiplicative inverse of a (mod m)
    using the extended Euclidean algorithm.
    """
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1


def encrypt(message, e, n):
    """Encrypt a message using the public key (e, n)."""
    cipher_text = [pow(ord(char), e, n) for char in message]
    return cipher_text


def decrypt(cipher_text, d, n):
    """Decrypt a message using the private key (d, n)."""
    decrypted_text = ''.join([chr(pow(char, d, n)) for char in cipher_text])
    return decrypted_text

# Generate two distinct prime numbers
p = q = 0
while not is_prime(p) or not is_prime(q):
    if not is_prime(p):
        p = random.randint(20, 100)
    if not is_prime(q):
        q = random.randint(20, 100)

# Calculate n = pq
n = p * q

# Print prime numbers
print("Prime numbers (p, q):", p, q)

# Calculate λ(n)
lambda_n = lcm(p - 1, q - 1)

# Print n and λ(n)
print("n:", n)
print("λ(n):", lambda_n)

# Choose a public exponent (e)
e = random.randint(2, lambda_n - 1)

# Ensure e is coprime to λ(n)
while gcd(e, lambda_n) != 1:
    e = random.randint(2, lambda_n - 1)

# Print public exponent (e)
print("Public exponent (e):", e)

# Calculate the modular multiplicative inverse of e (mod λ(n))
d = modinv(e, lambda_n)

print("Private exponent (d):", d)

# Sample message to encrypt
message = "Vamossss!"

cipher_text = encrypt(message, e, n)
print("Cipher text:", cipher_text)

decrypted_text = decrypt(cipher_text, d, n)
print("Decrypted text:", decrypted_text)
