import random
import json

# Dictionary that stores key as letters and value as number starting from 0
dic = {
    'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4,
    'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9,
    'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14,
    'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19,
    'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24,
    'z': 25
}

# Reverse of the dictionary used to convert number to text
rev_dic = {v: k for k, v in dic.items()}

def generate_random_key_matrix(block_size):
    """
    Generates a random invertible key matrix of the given block size.
    
    Args:
        block_size (int): The size of the key matrix (e.g., 2 for 2x2, 3 for 3x3).
    
    Returns:
        list: A randomly generated invertible key matrix.
    """
    while True:
        key_matrix = [[random.randint(0, 25) for _ in range(block_size)] for _ in range(block_size)]
        if determinant(key_matrix) != 0 and mod_inverse(determinant(key_matrix), 26) is not None:
            return key_matrix

def save_key_matrix(key_matrix, filename="key_matrix.json"):
    """
    Saves the key matrix to a file.
    
    Args:
        key_matrix (list): The key matrix to save.
        filename (str): The filename to save the key matrix as.
    """
    with open(filename, "w") as file:
        json.dump(key_matrix, file)

def load_key_matrix(filename="key_matrix.json"):
    """
    Loads the key matrix from a file.
    
    Args:
        filename (str): The filename to load the key matrix from.
    
    Returns:
        list: The loaded key matrix.
    """
    with open(filename, "r") as file:
        return json.load(file)

def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def get_cofactor(matrix, i, j):
    submatrix = [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]
    return ((-1) ** (i + j)) * determinant(submatrix)

def determinant(matrix):
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det = 0
    for c in range(len(matrix)):
        det += matrix[0][c] * get_cofactor(matrix, 0, c)
    return det % 26

def adjugate(matrix):
    adj = []
    for i in range(len(matrix)):
        adj_row = []
        for j in range(len(matrix)):
            cofactor = get_cofactor(matrix, i, j)
            adj_row.append(cofactor)
        adj.append(adj_row)
    return list(map(list, zip(*adj)))  # Transpose the matrix

def invert_key_matrix(key_matrix, block_size):
    det = determinant(key_matrix)
    det_inv = mod_inverse(det, 26)
    
    if det_inv is None:
        print("The key matrix is not invertible.")
        return
    
    adj = adjugate(key_matrix)
    inverted_matrix = [[(det_inv * adj[i][j]) % 26 for j in range(block_size)] for i in range(block_size)]
    
    return inverted_matrix

def encrypt(text, key_matrix, block_size, dic, rev_dic):
    encrypted_text = ''
    for i in range(0, len(text), block_size):
        block = [dic[char] for char in text[i:i + block_size]]
        encrypted_block = [(sum(key_matrix[j][l] * block[l] for l in range(block_size)) % 26) for j in range(block_size)]
        encrypted_text += ''.join(rev_dic[val] for val in encrypted_block)
    return encrypted_text

def decrypt(text, key_matrix, block_size, dic, rev_dic):
    decrypted_text = ''
    inv_key_matrix = invert_key_matrix(key_matrix, block_size)
    
    for i in range(0, len(text), block_size):
        block = [dic[char] for char in text[i:i + block_size]]
        decrypted_block = [(sum(inv_key_matrix[j][l] * block[l] for l in range(block_size)) % 26) for j in range(block_size)]
        decrypted_text += ''.join(rev_dic[val] for val in decrypted_block)
    return decrypted_text

should_continue = True
while should_continue:
    direction = input("Type 'e' to encrypt, type 'd' to decrypt: ").lower()
    text = input("Enter the text: ").lower().replace(" ", "")
    
    if direction == 'e':
        block_size = int(input("Enter the block size (e.g., 2 for 2x2 matrix): "))
        
        # Generate and save the key matrix
        key_matrix = generate_random_key_matrix(block_size)
        save_key_matrix(key_matrix)
        
        # Add filler at the end if the size of the text % block_size != 0
        while len(text) % block_size != 0:
            text += 'x'
        
        print("Key Matrix:")
        for row in key_matrix:
            print(row)
        
        result = encrypt(text, key_matrix, block_size, dic, rev_dic)
        print(f"The encoded text is {result}")
    
    elif direction == 'd':
        block_size = int(input("Enter the block size used for encryption: "))
        
        # Load the saved key matrix
        key_matrix = load_key_matrix()
        
        result = decrypt(text, key_matrix, block_size, dic, rev_dic)
        print(f"The decoded text is {result}")
    
    else:
        print("Invalid option. Please choose 'e' for encryption or 'd' for decryption.")
    
    c = input("Do you want to continue? Y or N: ").lower()
    if c == 'n':
        should_continue = False