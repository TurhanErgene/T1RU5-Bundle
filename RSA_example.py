import random

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Function to calculate the greatest common divisor of two numbers
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

# Function to calculate the modular multiplicative inverse of a number
def mod_inv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# Function to generate a key pair
def generate_key_pair():
    # Choose two random prime numbers
    p = random.randint(100, 1000)
    while not is_prime(p):
        p = random.randint(100, 1000)
    q = random.randint(100, 1000)
    while not is_prime(q):
        q = random.randint(100, 1000)

    # Calculate n and phi(n)
    n = p * q
    phi = (p-1) * (q-1)

    # Choose a random number e that is relatively prime to phi(n)
    e = random.randint(2, phi-1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi-1)

    # Calculate the modular multiplicative inverse of e mod phi(n)
    d = mod_inv(e, phi)

    # Return the public and private keys
    return ((n, e), (n, d))

# Function to encrypt a message using the public key
def encrypt(msg, public_key):
    n, e = public_key
    cipher = [pow(ord(char), e, n) for char in msg]
    return cipher

# Function to decrypt a message using the private key
def decrypt(cipher, private_key):
    n, d = private_key
    msg = [chr(pow(char, d, n)) for char in cipher]
    return ''.join(msg)

# Example usage
public_key, private_key = generate_key_pair()
message = "Hello, world!"
cipher = encrypt(message, public_key)
plaintext = decrypt(cipher, private_key)

print("Public key:", public_key)
print("Private key:", private_key)
print("Encrypted message:", cipher)
print("Decrypted message:", plaintext)