# Dictionary that stores key as letters and value as number starting from 0
dic = {
    'a': 0,'b': 1,'c': 2,'d': 3,'e': 4,
    'f': 5,'g': 6,'h': 7,'i': 8,'j': 9,
    'k': 10,'l': 11,'m': 12,'n': 13,'o': 14,
    'p': 15,'q': 16,'r': 17,'s': 18,'t': 19,
    'u': 20,'v': 21,'w': 22,'x': 23,'y': 24,
    'z': 25
}

#Reverse of the dictionary used to convert number to text
rev_dic={v:k for k,v in dic.items()}

should_continue=True

def create_matrix(text,size,dic):
    """
    Creates a matrix from the given text and dictionary.
    
    Args:
        text (str): The input text to be converted into a matrix.
        size (int): The size of the square matrix to be created.
        dic (dict): A dictionary mapping characters to their corresponding integer values.
    
    Returns:
        list: A 2D list representing the matrix.
    """
    matrix=[]
    for i in range(size):
        matrix.append([dic[text[size*i+j]]for j in range(size)])
    return matrix

def determinant(matrix, size):
    """ 
    Calculates the determinant of a square matrix of size `size`.
    
    Args:
        matrix (list): A 2D list representing the square matrix.
        size (int): The size of the square matrix.
    
    Returns:
        int: The determinant of the input matrix.
    """
    if size == 1:
        return matrix[0][0]
    if size == 2:
        return (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]) % 26
    result = 0
    for i in range(size):
        minor = [[matrix[r][c] for c in range(size) if c != i] for r in range(1, size)]
        result += ((-1) ** i) * matrix[0][i] * determinant(minor, size - 1)
    return result % 26

def adjoint(matrix, size):
    """
    Calculates the adjoint of a square matrix of size `size`.
    
    The adjoint of a matrix A is the transpose of the cofactor matrix of A. The cofactor matrix is a matrix where each element is the cofactor of the corresponding element in the original matrix.
    
    Args:
        matrix (list): A 2D list representing the square matrix.
        size (int): The size of the square matrix.
    
    Returns:
        list: A 2D list representing the adjoint of the input matrix.
    """
    adj = [[0] * size for _ in range(size)]
    if size == 1:
        adj[0][0] = 1
        return adj
    for i in range(size):
        for j in range(size):
            minor = [[matrix[r][c] for c in range(size) if c != j] for r in range(size) if r != i]
            sign = (-1) ** (i + j)
            adj[j][i] = (sign * determinant(minor, size - 1)) % 26
    return adj

def mod_inverse(determinant):
    """
    Calculates the modular inverse of a given determinant.
    
    The modular inverse of a number `a` modulo `m` is an integer `x` such that `(a * x) % m = 1`. This function finds the modular inverse of the given `determinant` modulo 26.
    
    Args:
        determinant (int): The determinant for which the modular inverse is to be calculated.
    
    Returns:
        int or None: The modular inverse of the `determinant` modulo 26, or `None` if the modular inverse does not exist.
    """
    determinant %= 26
    for i in range(1, 26):
        if (determinant * i) % 26 == 1:
            return i
    return None

def hillcipher(text, key_matrix, m, n, direction):
    """
    Performs Hill cipher encryption or decryption on the given plaintext or ciphertext using the provided key matrix.
    
    Args:
        text (str): The plaintext or ciphertext to be encrypted or decrypted.
        key_matrix (list): A 2D list representing the key matrix.
        m (int): The length of the plaintext or ciphertext.
        n (int): The size of the key matrix (square root of the length of the key).
        direction (str): The direction of the cipher operation, either 'e' for encryption or 'd' for decryption.
    
    Returns:
        str: The encrypted or decrypted text.
    """
    result = ''
    if direction == 'e':
        for i in range(0, m, n):
            text_group = text[i:i + n]
            text_matrix = [[dic[char]] for char in text_group]
            cipher_matrix = []
            for j in range(n):
                val = sum(key_matrix[j][l] * text_matrix[l][0] for l in range(n)) % 26
                cipher_matrix.append([val])
            for i in range(n):
                result += rev_dic[cipher_matrix[i][0]]
        print("Cipher Matrix:")
        for row in cipher_matrix:
            print(row)
    elif direction == 'd':
        det = determinant(key_matrix, n)
        det_inv = mod_inverse(det)
        if det_inv is None:
            print("Key matrix is not invertible")
            return 
        adj = adjoint(key_matrix, n)
        inv_key_matrix = [[(det_inv * adj[i][j]) % 26 for j in range(n)] for i in range(n)]
        for i in range(0, m, n):
            text_group = text[i:i + n]
            text_matrix = [[dic[char]] for char in text_group]
            plain_matrix = []
            for j in range(n):
                val = sum(inv_key_matrix[j][l] * text_matrix[l][0] for l in range(n)) % 26
                plain_matrix.append([val])
            for i in range(n):
                result += rev_dic[plain_matrix[i][0]]
        print("Plain Text Matrix:")
        for row in plain_matrix:
            print(row)
    return result
while should_continue:
    direction = input("Type 'e' to encrypt, type 'd' to decrypt: ").lower()
    pt=input("Enter the plain text: ").lower().replace(" ","")
    key=input("Enter the key: ").lower().replace(" ","")
    #Check if the length of the key is a perfect square
    if int(len(key)**0.5)**2!=len(key):
        print("Invalid key")
        key=input("Enter the valid input key: ").lower().replace(" ","")
        continue
    n=int(len(key)**0.5)
    m=len(pt)
    #Add filler at the end if the size of the plain text % square root of key length !=0
    while m%n!=0:
        pt+='x'
    key_matrix=create_matrix(key,n,dic)
    print("Key Matrix:")
    for row in key_matrix:
        print(row)
    result=hillcipher(pt,key_matrix,m,n,direction)
    if direction=='e':
        print(f"The encoded text is {result}")
    else:
        print(f"The decoded text is {result}")
    c=input("Do you want to continue? Y or N:\n")
    if c=='n':
        should_continue=False