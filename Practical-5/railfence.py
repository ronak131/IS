def create_matrix(plain_text,depth,direction):
    matrix=[["" for _ in range(len(plain_text))] for _ in range(depth)]
    row=0
    down=True
    for i in range(len(plain_text)):
        if direction=='e':
            matrix[row][i]=plain_text[i]
        else:
            matrix[row][i]='*'
        if down:
            if row==depth-1:
                down=False
                row-=1
            else:
                row+=1
        else:
            if row==0:
                down=True
                row+=1
            else:
                row-=1
    return matrix

def rail_fence(plain_text,depth,direction):
    result=""
    if direction=='e':
        matrix=create_matrix(plain_text,depth,direction)
        for i in range(depth):
            for j in range(len(plain_text)):
                if matrix[i][j]!="":
                    result+=matrix[i][j]
        for row in matrix:
            print(row)
    else:
        matrix=create_matrix(plain_text,depth,direction)
        i=0
        for r in range(depth):
            for c in range(len(plain_text)):
                if matrix[r][c]=='*':
                    matrix[r][c]=plain_text[i]
                    i+=1
        row=0
        down=True
        for i in range(len(plain_text)):
            result+=matrix[row][i]
            if down:
                if row==depth-1:
                    down=False
                    row-=1
                else:
                    row+=1
            else:
                if row==0:
                    down=True
                    row+=1
                else:
                    row-=1
        for row in matrix:
            print(row)
    return result
should_continue=True
while should_continue:
    direction = input("Type 'e' to encrypt, type 'd' to decrypt: ").lower()
    pt=input("Enter the plain text: ").lower().replace(" ","")
    depth=int(input("Enter the depth: "))
    result=rail_fence(pt,depth,direction)
    if direction=='e':
        print(f"The encoded text is {result}")
    else:
        print(f"The decoded text is {result}")
    c=input("Do you want to continue? Y or N:\n")
    if c=='n':
        should_continue=False