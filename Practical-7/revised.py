import random

dic = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5,
    'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
    'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15,
    'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
    'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,
    'z': 26
}

rev_dic = {v: k for k, v in dic.items()}

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_prime(min_value=100, max_value=500):
    """Generate a random prime number within a specified range."""
    while True:
        num = random.randint(min_value, max_value)
        if is_prime(num):
            return num

def mod_inverse(a, m):
    """Calculate the modular inverse of a with respect to m."""
    a %= m
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def gcd(a, b):
    """Calculate the Greatest Common Divisor (GCD) using the Euclidean algorithm."""
    if b == 0:
        return a
    return gcd(b, a % b)

def generate_key_pair():
    """Generate a unique public and private key pair."""
    p = generate_prime()
    q = generate_prime()
    n = p * q
    phi = (p - 1) * (q - 1)
    
    # Find e, the public exponent, that is coprime with phi
    for i in range(2, phi):
        if gcd(i, phi) == 1:
            e = i
            break
    
    # Calculate d, the modular inverse of e
    d = mod_inverse(e, phi)
    if d is None:
        return generate_key_pair()  # Recursively find a valid pair
    
    return (e, n), (d, n)

def rsa_encrypt_decrypt(text, key_pairs):
    """Encrypt and decrypt a text using variable key pairs."""
    cipher = []
    decrypted = []
    
    # Encrypt each character with its unique public key
    for idx, char in enumerate(text):
        if char not in dic:
            continue
        public_key, private_key = key_pairs[idx]
        cipher_value = (dic[char] ** public_key[0]) % public_key[1]
        cipher.append(cipher_value)
    
    # Decrypt each character with its corresponding private key
    for idx, cipher_value in enumerate(cipher):
        private_key = key_pairs[idx][1]
        decrypt_value = (cipher_value ** private_key[0]) % private_key[1]
        normalized_value = decrypt_value % 26
        if normalized_value == 0:
            normalized_value = 26  # Handle case when mod 26 results in 0
        decrypted.append(rev_dic[normalized_value])
    
    encrypted_text = ' '.join(str(i) for i in cipher)
    decrypted_text = ''.join(decrypted)
    
    return encrypted_text, decrypted_text

# Main loop to interact with the user
should_continue = True
while should_continue:
    # Input the text
    text = input("Type your message:\n").lower()
    
    # Generate a unique key pair for each character in the text
    key_pairs = [generate_key_pair() for _ in text]
    
    # Perform RSA encryption and decryption
    result = rsa_encrypt_decrypt(text, key_pairs)
    
    print(f"The encoded text is: {result[0]}")
    print(f"The decoded text is: {result[1]}")
    
    # Ask the user if they want to continue
    repeat = input("Do you want to go again? Y or N\n").lower()
    if repeat == 'n':
        should_continue = False