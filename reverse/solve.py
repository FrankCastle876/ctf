# Encrypted flag values in hex (from the Ghidra analysis)
encrypted_flag_1 = 0x3812081e1c213324
encrypted_flag_2 = 0x1a020a3813060205

# XOR key used during encryption
key = 0x67

# Function to decrypt each byte of the 8-byte value and print intermediate steps
def xor_decrypt(value, key):
    decrypted_bytes = []
    for i in range(8):
        # Extract each byte by shifting and masking
        byte = (value >> (i * 8)) & 0xFF
        # XOR the byte with the key and store it
        decrypted_byte = byte ^ key
        decrypted_bytes.append(decrypted_byte)
        # Print out the result for each byte
        print(f"Byte {i}: Encrypted {hex(byte)} -> Decrypted {hex(decrypted_byte)}")
    return bytes(decrypted_bytes)

# Decrypt both parts of the flag (local_98 and local_90)
decrypted_flag_1 = xor_decrypt(encrypted_flag_1, key)
decrypted_flag_2 = xor_decrypt(encrypted_flag_2, key)

# Combine the two decrypted parts (since it's an 8-byte flag split into two 8-byte parts)
full_decrypted_flag = decrypted_flag_1 + decrypted_flag_2

# Convert bytes to string and print the result
print("\nDecrypted Flag (Hex):", full_decrypted_flag.hex())
print("Decrypted Flag (Text):", full_decrypted_flag.decode('utf-8', errors='ignore'))
