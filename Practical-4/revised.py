dic = {
    'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4,
    'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9,
    'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14,
    'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19,
    'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24,
    'z': 25
}

def geometric_progression_shift(key_length):
    # Calculate the geometric progression shift for the length of the key with the common ratio = key length
    return sum(key_length**i for i in range(key_length)) % 26

def vignere_cipher_gp(key, plain_text, direction):
    result = []
    cipher = ""
    m = len(plain_text)
    n = len(key)
    
    # Calculate the GP-based shift
    gp_shift = geometric_progression_shift(n)
    
    for i in range(m):
        if plain_text[i] not in dic:
            result.append(plain_text[i])
        else:
            key_value = dic[key[i % n]]
            if direction == 'e':
                # Encrypt by shifting the plain text letter by the key letter's value plus GP shift
                result.append((dic[plain_text[i]] + key_value + gp_shift) % 26)
            else:
                # Decrypt by shifting the plain text letter backward by the key letter's value plus GP shift
                result.append((dic[plain_text[i]] - key_value - gp_shift) % 26)
    
    for num in result:
        if isinstance(num, int):  # Convert numbers back to letters
            for k, v in dic.items():
                if v == num:
                    cipher += k
                    break
        else:
            cipher += num
    
    return cipher

# Main loop for user interaction
should_continue = True
while should_continue:
    direction = input("Type 'e' to encrypt, type 'd' to decrypt: ").lower()
    pt = input("Enter the plain text: ").lower().replace(" ", "")
    key = input("Enter the key: ").lower().replace(" ", "")
    result = vignere_cipher_gp(key, pt, direction)
    
    if direction == 'e':
        print(f"The encoded text is {result}")
    else:
        print(f"The decoded text is {result}")
    
    c = input("Do you want to continue? Y or N:\n").lower()
    if c == 'n':
        should_continue = False