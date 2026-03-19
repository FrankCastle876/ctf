#include <stdio.h>
#include <string.h>

// Simple XOR function
char* xor_fxn(char *data, size_t len, char key) {
    for (size_t i = 0; i < len; i++) {
        data[i] ^= key;
        return data;
    }
}

int main() {
    // Encrypted flag (XOR-encrypted version of "CTF{you_beat_me}")
    unsigned char encrypted_flag[] = { 0x24,0x33,0x21,0x1c,0x1e,0x08,0x12,0x38,0x05,0x02,0x06,0x13,0x38,0x0a,0x02,0x1a };

    // XOR key (hidden in code)
    unsigned char key = 0x67;

   // Allocate space for the decrypted flag (same size as the encrypted flag)
    unsigned char internal_flag[sizeof(encrypted_flag)];

    // Decrypt the flag internally
    xor_fxn((char *)encrypted_flag, sizeof(encrypted_flag), key);

    char user_input[100];  // Buffer to store user input

    // Ask user to input the flag
    printf("Enter the flag: ");
    fgets(user_input, sizeof(user_input), stdin);

    // Remove any extra newline from the user input (from fgets)
    user_input[strcspn(user_input, "\n")] = '\0';

    // Check if the user's input matches the correct flag
    if (strcmp(user_input, internal_flag) == 0) {
        printf("Congratulations! You solved the challenge!\n");
    } else {
        printf("Incorrect flag. Try again.\n");
    }

    return 0;
}