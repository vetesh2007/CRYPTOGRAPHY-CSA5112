def generate_matrix(keyword):
    matrix = []
    keyword = "".join(sorted(set(keyword.upper()), key=keyword.index)).replace("J", "I")
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for c in keyword:
        if c not in matrix:
            matrix.append(c)
    for c in alphabet:
        if c not in matrix:
            matrix.append(c)
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, char):
    for i, row in enumerate(matrix):
        for j, c in enumerate(row):
            if c == char:
                return i, j

def playfair_encrypt(text, matrix):
    text = text.upper().replace("J", "I").replace(" ", "")
    if len(text) % 2 != 0:
        text += "X"
    ciphertext = ""
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)
        if row1 == row2:
            ciphertext += matrix[row1][(col1 + 1) % 5]
            ciphertext += matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += matrix[(row1 + 1) % 5][col1]
            ciphertext += matrix[(row2 + 1) % 5][col2]
        else:
            ciphertext += matrix[row1][col2]
            ciphertext += matrix[row2][col1]
    return ciphertext

# Example
keyword = input("Enter keyword: ")
matrix = generate_matrix(keyword)
plaintext = input("Enter plaintext: ")
ciphertext = playfair_encrypt(plaintext, matrix)
print("Ciphertext:", ciphertext)
