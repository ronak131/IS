import hashlib
import secrets

# Function to compute modular inverse
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# DSA key generation
def generate_keys(p, q):
    g = secrets.randbelow(p - 2) + 2
    x = secrets.randbelow(q - 1) + 1
    y = pow(g, x, p)
    return (p, q, g, y), x  # Public key and private key

# Hash message using SHA-256
def hash_message(message):
    return int(hashlib.sha256(message.encode()).hexdigest(), 16)

# Sign the message
def sign_message(message, private_key, p, q, g):
    x = private_key
    message_hash = hash_message(message)
    while True:
        k = secrets.randbelow(q - 1) + 1
        r = pow(g, k, p) % q
        if r == 0:
            continue
        k_inv = mod_inverse(k, q)
        s = (k_inv * (message_hash + x * r)) % q
        if s == 0:
            continue
        break
    return (r, s)

# Verify the signature
def verify_signature(message, signature, public_key, p, q, g):
    r, s = signature
    y = public_key
    message_hash = hash_message(message)

    if not (0 < r < q and 0 < s < q):
        return False

    w = mod_inverse(s, q)
    u1 = (message_hash * w) % q
    u2 = (r * w) % q
    v = ((pow(g, u1, p) * pow(y, u2, p)) % p) % q

    # Debug statements
    print(f"message_hash: {message_hash}")
    print(f"w: {w}, u1: {u1}, u2: {u2}, v: {v}")

    return v == r

message = input("Enter the message to be signed: ")
p = int(input("Enter the large prime number (p): "))
q = int(input("Enter the prime number which is the divisor of p-1: "))

# Generate keys
public_key, private_key = generate_keys(p, q)
print(f"Public Key (p, q, g, y): {public_key}")
print(f"Private Key (x): {private_key}")

# Sign the message
signature = sign_message(message, private_key, public_key[0], public_key[1], public_key[2])
print(f"Signature: {signature}")

# Ask user if they want to verify the signature
verify = input("Do you want to verify the signature? (yes/no): ").lower()

if verify == 'yes':
    is_valid = verify_signature(message, signature, public_key[3], public_key[0], public_key[1], public_key[2])
    print(f"Signature Valid: {is_valid}")
else:
    print("Signature verification skipped.")
