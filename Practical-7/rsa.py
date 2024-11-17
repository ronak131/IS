dic = {
    'a': 1,'b': 2,'c': 3,'d': 4,'e': 5,
    'f': 6,'g': 7,'h': 8,'i': 9,'j': 10,
    'k': 11,'l': 12,'m': 13,'n': 14,'o': 15,
    'p': 16,'q': 17,'r': 18,'s': 19,'t': 20,
    'u': 21,'v': 22,'w': 23,'x': 24,'y': 25,
    'z': 26
}

rev_dic={v:k for k,v in dic.items()}

def isPrime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def mod_inverse(a,m):
    a%=m
    for i in range(1,m):
        if (a*i)%m==1:
            return i
    return None

def gcd(a,b):
    if b==0:
        return a 
    return gcd(b,a%b)

def generate_keys(p,q):
    n=p*q
    phi=(p-1)*(q-1)
    for i in range(2,phi):
        if gcd(i,phi)==1:
            e=i
            break
    d=mod_inverse(e,phi)
    if d==None:
        print("No modular inverse found")
        return None
    return (e,n),(d,n)

def rsa(text,public_key,private_key):
    cipher=[]
    for char in text:
        cipher.append((dic[char]**public_key[0])%public_key[1])
    encrypt=''.join(str(i) for i in cipher)
    decipher=[]
    for i in cipher:
        decipher.append(rev_dic[(i**private_key[0])%private_key[1]])
    decrypt=''.join(decipher)
    return encrypt,decrypt

should_continue=True
while should_continue:
    text = input("Type your message:\n").lower()
    p=int(input("Enter the 1st big prime number: "))
    q=int(input("Enter the 2nd big prime number: "))
    if not isPrime(p) and not isPrime(q):
        print("Both numbers are not prime")
        continue
    public_key,private_key=generate_keys(p,q)
    result = rsa(text,public_key,private_key)

    print(f"The encoded text is {result[0]}")
    print(f"The decoded text is {result[1]}")
    
    repeat = input("Do you want to go again? Y or N\n").lower()
    if repeat == 'n':
        should_continue = False