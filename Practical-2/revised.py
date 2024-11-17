import numpy as np

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#Converts the text in to list of two characters
def GroupOfTwo(text):
    res=[]
    group=0
    for i in range(2,len(text),2):
        res.append(text[group:i])
        group=i
    res.append(text[group:])
    return res

#Adds filler character 'x' between two same characters 
def Filler(text,direction):
    n = len(text)
    if direction=='e':
        if n % 2 == 0:
            for i in range(0, n, 2):
                if text[i] == text[i+1]:
                    new_word = text[:i+1] + 'x' + text[i+1:]
                    new_word = Filler(new_word)
                    break
                else:
                    new_word = text
        else:
            for i in range(0, n-1, 2):
                if text[i] == text[i+1]:
                    new_word = text[:i+1] + 'x' + text[i+1:]
                    new_word = Filler(new_word)
                    break
                else:
                    new_word = text
        if len(new_word)%2!=0:
            new_word+='x'
    else:
        for i in range(0, n, 2):
                if text[i] == text[i+1]:
                    new_word = text[:i+1] + 'x' + text[i+1:]
                    new_word = Filler(new_word)
                    break
                else:
                    new_word = text
    return new_word

#New Row rule
def row(matrix,r1,c1,r2,c2,direction):
    char1,char2='',''
    if direction=='e':
        char1=matrix[(r1+1)%5][c1]
        char2=matrix[(r2+1)%5][c2]
    else:
        char1=matrix[(r1-1)%5][c1]
        char2=matrix[(r2-1)%5][c2]
    return char1,char2

#New Column rule
def column(matrix,r1,c1,r2,c2,direction):
    char1,char2='',''
    if direction=='e':
        char1=matrix[r1][(c1+1)%5]
        char2=matrix[r2][(c2+1)%5]
    else:
        char1=matrix[r1][(c1-1)%5]
        char2=matrix[r2][(c2-1)%5]
    return char1,char2

#New Rectangle rule
def Rectangle(matrix,r1,c1,r2,c2,direction):
    if direction=="e":
        return matrix[(r1+1)%5][(c1+1)%5],matrix[(r2+1)%5][(c2+1)%5]
    else:
        return matrix[(r1-1)%5][(c1-1)%5],matrix[(r2-1)%5][(c2-1)%5]

#Encryption/Decryption by Revised Playfair Cipher
def playfair(matrix,digrams,direction):
    res=[]
    ans=''
    for i in range(len(digrams)):
        c1=0
        c2=0
        for j in range(5):
              for k in range(5):
                  if matrix[j][k]==digrams[i][0]:
                      e1x,e1y=j,k
        for j in range(5):
              for k in range(5):
                  if matrix[j][k]==digrams[i][1]:
                      e2x,e2y=j,k
        if e1x==e2x:
            c1,c2=row(matrix,e1x,e1y,e2x,e2y,direction)
        elif e1y==e2y:
            c1,c2=column(matrix,e1x,e1y,e2x,e2y,direction)
        else:
            c1,c2=Rectangle(matrix,e1x,e1y,e2x,e2y,direction)
        cipher=c1+c2
        res.append(cipher)
    
    for i in res:
        ans+=i
        if direction=='e':
            ans+=' '
    return ans  

should_continue=True
while should_continue:
    direction = input("Type 'e' to encrypt, type 'd' to decrypt: ").lower()
    plain_text = input("Type your message: ").lower()
    plain_text=plain_text.replace(" ","")
    key = (input("Enter the key: ")).lower()
    
    #Create a 5x5 matrix with the unique letters in key and rest of the letter in the alphabet
    key_letter=[]
    composite=[]
    matrix=[]
    for i in key:
        if i not in key_letter:
            key_letter.append(i)
    for i in key_letter:
        if i not in composite:
            composite.append(i)
    for i in alphabet:
        if i not in composite:
            composite.append(i)
    for i in range(0,25,5):
        matrix.append(composite[i:i+5])
    print("Matrix: ")
    print(np.matrix(matrix))
    
    digrams=GroupOfTwo(Filler(plain_text,direction))
    print(f"Digrams : {digrams}")
    
    result=playfair(matrix,digrams,direction)
    if direction == 'e':
        print(f"The encoded text is {result}")
    elif direction == 'd':
        print(f"The decoded text is {result}")
        
    repeat = input("Do you want to go again? Y or N\n").lower()
    if repeat == 'n':
        should_continue = False