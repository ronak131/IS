def rail_fence_revised(plaintext, depth, direction):
    result = ""
    n = len(plaintext)
    if depth == 1:
        return plaintext
    if direction == 'e': 
        rows = ['' for _ in range(depth)]
        row = 0
        down = True
        for char in plaintext:
            rows[row] += char
            if down:
                if row == depth - 1:
                    down = False
                    row -= 1
                else:
                    row += 1
            else:
                if row == 0:
                    down = True
                    row += 1
                else:
                    row -= 1
        for row in rows:
            result += row

    else:  
        rows_len = [0] * depth
        row = 0
        down = True
        for i in range(n):
            rows_len[row] += 1
            if down:
                if row == depth - 1:
                    down = False
                    row -= 1
                else:
                    row += 1
            else:
                if row == 0:
                    down = True
                    row += 1
                else:
                    row -= 1
        rows = [''] * depth
        index = 0
        for i in range(depth):
            rows[i] = plaintext[index:index + rows_len[i]]
            index += rows_len[i]
        rows_indices = [0] * depth
        row = 0
        down = True
        for i in range(n):
            result += rows[row][rows_indices[row]]
            rows_indices[row] += 1
            if down:
                if row == depth - 1:
                    down = False
                    row -= 1
                else:
                    row += 1
            else:
                if row == 0:
                    down = True
                    row += 1
                else:
                    row -= 1
    return result

should_continue = True
while should_continue:
    direction = input("Type 'e' to encrypt, type 'd' to decrypt: ").lower()
    pt = input("Enter the plain text: ").lower().replace(" ", "")
    depth = int(input("Enter the depth: "))
    result = rail_fence_revised(pt, depth, direction)
    if direction == 'e':
        print(f"The encoded text is {result}")
    else:
        print(f"The decoded text is {result}")
    c = input("Do you want to continue? Y or N:\n").lower()
    if c == 'n':
        should_continue = False