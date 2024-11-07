
def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    if mode == 'decrypt':
        shift = -shift
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) + shift - shift_base) % 26 + shift_base)
        else:
            result += char
    return result

if __name__ == "__main__":
    message = input("Enter message: ")
    shift = int(input("Enter shift: "))
    mode = input("Enter mode (encrypt/decrypt): ").strip().lower()
    encrypted_message = caesar_cipher(message, shift, mode)
    print(f"{mode.capitalize()}ed message: {encrypted_message}")
