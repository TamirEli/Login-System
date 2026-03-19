import hashlib


def calculate_bits(string):
    # Assuming UTF-8 encoding
    byte_size = len(string.encode('utf-8'))
    bits = byte_size * 8
    return bits


def divide_string_into_256_bits(input_string):
    # Convert the string to bytes using a specific encoding (e.g., UTF-8)
    encoded_bytes = input_string.encode('utf-8')

    # Use a hashlib function (e.g., SHA-256) to create a hash
    hash_object = hashlib.sha256(encoded_bytes)
    hash_hex = hash_object.hexdigest()

    # Split the hash into 256-bit chunks (32 bytes)
    chunk_size = 32
    chunks = [hash_hex[i:i + chunk_size] for i in range(0, len(hash_hex), chunk_size)]  # do a list

    return chunks, hash_hex


my_string = input("Enter a string: ")
hash_list, str_hash = divide_string_into_256_bits(my_string)  # Hash list by blocks

print("The string after hash:")
print(hash_list)
print(str_hash)



