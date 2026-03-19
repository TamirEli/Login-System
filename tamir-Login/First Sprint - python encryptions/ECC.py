import random
from typing import Tuple, Union


# Elliptic Curve parameters

p = 29  # Prime field
G = (4, 8)  # Base point

# Point at infinity
O = "infinity"


def point_addition(P: Tuple[int, int], Q: Union[str, Tuple[int, int]], a: int) -> Tuple[int, int]:
    if P == O:
        return Q

    if Q == O:
        return P

    if P[0] == Q[0] and P[1] != Q[1]:
        return O

    if P[0] != Q[0]:
        m = (Q[1] - P[1]) * pow(Q[0] - P[0], -1, p)
    else:
        m = (3 * pow(P[0], 2) + a) * pow(2 * P[1], -1, p)

    # Calculate the new coordinates (x, y) after the point addition
    x_res = (pow(m, 2) - P[0] - Q[0]) % p
    y_res = (m * (P[0] - x_res) - P[1]) % p

    return x_res, y_res


def scalar_multiply(k: int, P: Tuple[int, int], a:int) -> Tuple[int, int]:
    # double and add algorithm
    result = O
    for i in range(k.bit_length()):
        if k & 1:
            # adding point for each bit of the scalar
            result = point_addition(result, P, a)
        # double the point for the next bit of the scalar
        P = point_addition(P, P, a)
        k >>= 1
    return result


def generate_key_pair(a:int) -> Tuple[int, Tuple[int, int]]:
    # Generate a random private key
    private_key = random.randint(1, p - 1)
    # Calculate the corresponding public key by scalar multiplication with the base point G
    public_key = scalar_multiply(private_key, G, a)
    return private_key, public_key


def encrypt(message: str, recipient_public_key: Tuple[int, int], a: int) -> Tuple[str, Tuple[int, int]]:
    ephemeral_private_key = random.randint(1, p - 1)
    ephemeral_public_key = scalar_multiply(ephemeral_private_key, G, a)

    shared_secret = scalar_multiply(ephemeral_private_key, recipient_public_key, a)

    symmetric_key = shared_secret[0]

    encrypted_message = ''.join([chr(ord(char) ^ symmetric_key) for char in message])

    return encrypted_message, ephemeral_public_key


def decrypt(encrypted_message: str, private_key: int, ephemeral_public_key: Tuple[int, int], a: int) -> str:
    shared_secret = scalar_multiply(private_key, ephemeral_public_key, a)

    symmetric_key = shared_secret[0]

    decrypted_message = ''.join([chr(ord(char) ^ symmetric_key) for char in encrypted_message])

    return decrypted_message


a = 1


private_key, public_key = generate_key_pair(a)

message = "abcde"
encrypted_message, ephemeral_public_key = encrypt(message, public_key, a)

decrypted_message = decrypt(encrypted_message, private_key, ephemeral_public_key, a)

print("Encrypted message:", encrypted_message)
print("Decrypted message:", decrypted_message)
