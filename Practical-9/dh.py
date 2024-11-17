def main():
    p=int(input("Enter the 1st public number(ie. prime number): "))
    g=int(input("Enter the 2nd public number(ie. a generator of prime number): "))
    sender_pvt=int(input('Enter the sender\'s private number: '))
    reciever_pvt=int(input('Enter the reciever\'s private number: '))
    x=(g**sender_pvt)%p
    y=(g**reciever_pvt)%p
    ks=(y**sender_pvt)%p
    kr=(x**reciever_pvt)%p
    print(f"Public key of Sender & Reciever:({p},{g})")
    print(f"Private key of Sender:{sender_pvt}")
    print(f"Private key of Reciever:{reciever_pvt}")
    print(f"Key generated for sender: {x}")
    print(f"Key generated for reciever: {y}")
    print("Exchanging generated keys......")
    print(f"Secret key for sender: {ks}")
    print(f"Secret key for reciever: {kr}")

if __name__ == '__main__':
    main()