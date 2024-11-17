# Function to perform calculation during encryption 
def calculate(plain_text,key):
    result=""
    m=len(plain_text)
    n=len(key)
    for i in range(m):
        char=ord(plain_text[i])
        new_char=chr(char+int(key[i%n]))
        result+=new_char
    return result

# Function to add padding in the plain text 
def padding(plain_text,key):
    m=len(plain_text)
    n=len(key)
    last_char=plain_text[m-1]
    if m%n!=0:
        return padding(plain_text+last_char,key)
    return plain_text

# Function to encrypt using functions created above
def encrypt(plain_text,key):
    m=len(plain_text)
    n=len(key)
    if m!=n:
        plain_text=padding(plain_text,key)
    return calculate(plain_text,key)

# Main function to ask user input and print encrypted result
def main():
    plain_text=input("Enter the plain_text: ")
    key=input("Enter the key: ")
    result=encrypt(plain_text,key)
    print(f"Encrypted Text: {result}")
    
if __name__ == '__main__':
    main()