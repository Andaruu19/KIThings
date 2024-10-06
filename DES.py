IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

FP = [40, 8, 48, 16, 56, 24, 64, 32,
      39, 7, 47, 15, 55, 23, 63, 31,
      38, 6, 46, 14, 54, 22, 62, 30,
      37, 5, 45, 13, 53, 21, 61, 29,
      36, 4, 44, 12, 52, 20, 60, 28,
      35, 3, 43, 11, 51, 19, 59, 27,
      34, 2, 42, 10, 50, 18, 58, 26,
      33, 1, 41, 9, 49, 17, 57, 25]

PC1 = [57, 49, 41, 33, 25, 17, 9,
       1, 58, 50, 42, 34, 26, 18,
       10, 2, 59, 51, 43, 35, 27,
       19, 11, 3, 60, 52, 44, 36,
       63, 55, 47, 39, 31, 23, 15,
       7, 62, 54, 46, 38, 30, 22,
       14, 6, 61, 53, 45, 37, 29,
       21, 13, 5, 28, 20, 12, 4]

PC2 = [14, 17, 11, 24, 1, 5,
       3, 28, 15, 6, 21, 10,
       23, 19, 12, 4, 26, 8,
       16, 7, 27, 20, 13, 2,
       41, 52, 31, 37, 47, 55,
       30, 40, 51, 45, 33, 48,
       44, 49, 39, 56, 34, 53,
       46, 42, 50, 36, 29, 32]

E = [32, 1, 2, 3, 4, 5, 4, 5,
     6, 7, 8, 9, 8, 9, 10, 11,
     12, 13, 12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21, 20, 21,
     22, 23, 24, 25, 24, 25, 26, 27,
     28, 29, 28, 29, 30, 31, 32, 1]


P = [16, 7, 20, 21,
     29, 12, 28, 17,
     1, 15, 23, 26,
     5, 18, 31, 10,
     2, 8, 24, 14,
     32, 27, 3, 9,
     19, 13, 30, 6,
     22, 11, 4, 25]

S_BOX = [
    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
     [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
     [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
     [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],

    # S2
    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
     [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
     [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
     [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],

    # S3
    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
     [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
     [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
     [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],

    # S4
    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
     [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
     [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
     [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],

    # S5
    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
     [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
     [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
     [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],

    # S6
    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
     [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
     [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
     [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],

    # S7
    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
     [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
     [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
     [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],

    # S8
    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
     [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
     [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
     [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
]

SHIFTS = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

def permute(block, table):
    return [block[i - 1] for i in table]

def left_shift(key, shift):
    return key[shift:] + key[:shift]

def xor(bits1, bits2):
    return [b1 ^ b2 for b1, b2 in zip(bits1, bits2)]

def sbox_substitution(expanded_half_block):
    output = []
    for i in range(8):
        block = expanded_half_block[i * 6: (i + 1) * 6]
        row = (block[0] << 1) + block[5]
        col = (block[1] << 3) + (block[2] << 2) + (block[3] << 1) + block[4]
        sbox_val = S_BOX[i][row][col]
        output += [int(bit) for bit in format(sbox_val, '04b')]
    return output

def feistel_function(right_half, sub_key):
    expanded_right = permute(right_half, E)
    xor_result = xor(expanded_right, sub_key)
    substituted = sbox_substitution(xor_result)
    
    return permute(substituted, P)

def key_schedule(initial_key):
    permuted_key = permute(initial_key, PC1)
    
    left, right = permuted_key[:28], permuted_key[28:]
    
    sub_keys = []
    for shift in SHIFTS:
        left = left_shift(left, shift)
        right = left_shift(right, shift)
        sub_keys.append(permute(left + right, PC2))
    
    return sub_keys

def des_round(left_half, right_half, sub_key):
    new_left = right_half
    new_right = xor(left_half, feistel_function(right_half, sub_key))
    
    return new_left, new_right

def des_encrypt_block(plain_block, sub_keys):
    block = permute(plain_block, IP)
    left, right = block[:32], block[32:]
    
    for sub_key in sub_keys:
        left, right = des_round(left, right, sub_key)
    
    combined_block = right + left
    cipher_block = permute(combined_block, FP)
    
    return cipher_block

def des_decrypt_block(cipher_block, sub_keys):
    block = permute(cipher_block, IP)
    left, right = block[:32], block[32:]
    
    for sub_key in reversed(sub_keys):
        left, right = des_round(left, right, sub_key)
    
    combined_block = right + left
    plain_block = permute(combined_block, FP)
    
    return plain_block

def string_to_bit_array(string):
    bit_array = []
    for char in string:
        bin_value = format(ord(char), '08b')
        bit_array.extend([int(bit) for bit in bin_value])
    return bit_array

def bit_array_to_string(bit_array):
    string = ''.join(chr(int(''.join(map(str, bit_array[i:i+8])), 2)) for i in range(0, len(bit_array), 8))
    return string

def is_textlength_8(text):
    while len(text) % 8 != 0:
        text += ' '
    return text

def des_encrypt(plaintext, key):
    plaintext = is_textlength_8(plaintext)
    plain_bits = string_to_bit_array(plaintext)
    key_bits = string_to_bit_array(key)
    sub_keys = key_schedule(key_bits)
    cipher_bits = des_encrypt_block(plain_bits, sub_keys)
  
    return bit_array_to_string(cipher_bits)

def des_decrypt(ciphertext, key):
    cipher_bits = string_to_bit_array(ciphertext)
    key_bits = string_to_bit_array(key)
    sub_keys = key_schedule(key_bits)
    plain_bits = des_decrypt_block(cipher_bits, sub_keys)
    
    return bit_array_to_string(plain_bits).rstrip()

if __name__ == "__main__":
    plaintext = "kimjiwon"
    key = "jawajawa"
    
    print(f"Plaintext: {plaintext}")
    
    # Enkripsi
    cipher = des_encrypt(plaintext, key)
    print(f"Ciphertext: {cipher}")
    
    # Dekripsi
    decrypted = des_decrypt(cipher, key)
    print(f"Decrypted Text: {decrypted}")
