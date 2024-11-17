#Create a list of fibonacci number of size of text
def generate_fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

def caesar_with_fibonacci(start_text, cipher_direction):
    n = len(start_text)
    fib_sequence = generate_fibonacci(n)
    end_text = ""
    for i in range(n):
        char = start_text[i]
        shift_amount = fib_sequence[i] % 26  
        if char in alphabet:
            position = alphabet.index(char)
            if cipher_direction == "e":
                new_position = (position + shift_amount) % len(alphabet)
            elif cipher_direction == "d":
                new_position = (position - shift_amount) % len(alphabet)
            end_text += alphabet[new_position]
        else:
            end_text += char
    return end_text

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
should_continue = True

while should_continue:
    direction = input("Type 'e' to encrypt, type 'd' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    
    result = caesar_with_fibonacci(start_text = text, cipher_direction = direction)
    if direction == 'e':
        print(f"The encoded text is {result}")
    elif direction == 'd':
        print(f"The decoded text is {result}")
    
    repeat = input("Do you want to go again? Y or N\n").lower()
    if repeat == 'n':
        should_continue = False