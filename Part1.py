# implement a python function caesar_cipher that takes in three arguments: a string message, an integer shift, and a boolean encode.
def caesar_cipher(message, shift, encrypt=True):
    result = ""
    if not encrypt:
        shift = -shift


    for char in message:
        #shift characters in ASCII range 32 to 126
        ascii_val = ord(char)
        if 32 <= ascii_val <= 126:

            result += chr((ascii_val - 32 + shift) % 95 + 32)
        else:
            # Keep characters outside this range unchanged
            result += char
    return result

def vigenere_cipher(message, keyword, encrypt=True):
    result = ""
    keyword_index = 0

    for char in message:
        ascii_val = ord(char)

        if 32 <= ascii_val <= 126:
            
            shift = ord(keyword[keyword_index % len(keyword)]) - 32
            
            result += caesar_cipher(char, shift, encrypt)
            keyword_index += 1
        else:
            result += char

    return result


def main():
    print("=== Caesar Cipher Test ===")
    message = "Hello World!"
    shift = 5
    
    encrypted = caesar_cipher(message, shift, encrypt=True)
    print(f"Original:  {message}")
    print(f"Encrypted: {encrypted}")
    
    decrypted = caesar_cipher(encrypted, shift, encrypt=False)
    print(f"Decrypted: {decrypted}")
    
    print("\n=== Vigenere Cipher Test ===")
    keyword = "KEY"
    
    encrypted_vig = vigenere_cipher(message, keyword, encrypt=True)
    print(f"Original:  {message}")
    print(f"Encrypted: {encrypted_vig}")
    
    decrypted_vig = vigenere_cipher(encrypted_vig, keyword, encrypt=False)
    print(f"Decrypted: {decrypted_vig}")
if __name__ == "__main__":
    main()