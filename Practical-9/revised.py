import hashlib

def generate_key_hash(key):
    # Convert key to string, encode it, and create SHA-256 hash
    key_str = str(key).encode()
    return hashlib.sha256(key_str).hexdigest()

def main():
    p = int(input("Enter the 1st public number (i.e., prime number): "))
    g = int(input("Enter the 2nd public number (i.e., a generator of prime number): "))
    sender_pvt = int(input("Enter the sender's private number: "))
    receiver_pvt = int(input("Enter the receiver's private number: "))
    
    # Generate public keys
    x = (g ** sender_pvt) % p
    y = (g ** receiver_pvt) % p
    
    # Create a checksum (hash) for each key
    sender_hash = generate_key_hash(x)
    receiver_hash = generate_key_hash(y)
    
    # Display public keys and their hashes
    print(f"Public key of Sender & Receiver: ({p}, {g})")
    print(f"Private key of Sender: {sender_pvt}")
    print(f"Private key of Receiver: {receiver_pvt}")
    print(f"Key generated for Sender: {x} (Hash: {sender_hash})")
    print(f"Key generated for Receiver: {y} (Hash: {receiver_hash})")
    
    # Verify hashes before exchanging keys
    print("Exchanging generated keys and verifying integrity...")
    if generate_key_hash(y) == receiver_hash and generate_key_hash(x) == sender_hash:
        print("Keys verified successfully.")
        
        # Calculate shared secret keys
        ks = (y ** sender_pvt) % p
        kr = (x ** receiver_pvt) % p
        
        print(f"Secret key for Sender: {ks}")
        print(f"Secret key for Receiver: {kr}")
    else:
        print("Error: Key verification failed. Keys may have been tampered with.")

if __name__ == '__main__':
    main()