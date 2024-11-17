alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
should_continue = True

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    for char in start_text:
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

while should_continue:
    direction = input("Type 'e' to encrypt, type 'd' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 26
    
    result = caesar(start_text = text, shift_amount = shift, cipher_direction = direction)
    if direction == 'e':
        print(f"The encoded text is {result}")
    elif direction == 'd':
        print(f"The decoded text is {result}")
    
    repeat = input("Do you want to go again? Y or N\n").lower()
    if repeat == 'n':
        should_continue = False