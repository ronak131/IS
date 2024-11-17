dic = {
    'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4,
    'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9,
    'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14,
    'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19,
    'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24,
    'z': 25
}
def vignere_cipher(key, plain_text, direction):
    result = []
    cipher = ""
    m = len(plain_text)
    n = len(key)
    for i in range(m):
        # For adding non-alphabetic character to the result
        if plain_text[i] not in dic:
            result.append(plain_text[i])
        else:
            #Encrypt each letter with the corresponding letter of the key by shifting the letter by the corresponding number of alphabetic positions
            if direction == 'e':
                result.append((dic[plain_text[i]] + dic[key[i % n]]) % 26)
            else:
                #Decrypt each letter with the corresponding letter of the key by shifting backward
                result.append((dic[plain_text[i]] - dic[key[i % n]]) % 26)
    for num in result:
        if isinstance(num, int): #check if the result is an integer 
            for k, v in dic.items():
                if v == num:
                    cipher += k
                    break
        else:
            cipher += num 
    return cipher

should_continue = True
while should_continue:
    direction = input("Type 'e' to encrypt, type 'd' to decrypt: ").lower()
    pt = input("Enter the plain text: ").lower()
    key = input("Enter the key: ").lower().replace(" ", "")
    result = vignere_cipher(key, pt, direction)
    if direction == 'e':
        print(f"The encoded text is {result}")
    else:
        print(f"The decoded text is {result}")
    c = input("Do you want to continue? Y or N:\n").lower()
    if c == 'n':
        should_continue = False