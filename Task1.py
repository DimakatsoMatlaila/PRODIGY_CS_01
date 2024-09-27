def caesarCipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            shiftAmount = shift if mode == 1 else -shift
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shiftAmount) % 26 + base)
        else:
            result += char
    return result

def bruteForce(text):
    for shift in range(1, 27):
        print(f"Shift {shift}: {caesarCipher(text, shift, 2)}")

def main():
    print("Choose an option:")
    print("1. Encrypt")
    print("2. Decrypt")
    mode = int(input())
    text = input("Enter the message: ")
    if mode == 1:
        shift = int(input("Enter the shift value: "))
        print("Result:", caesarCipher(text, shift, mode))
    elif mode == 2:
        print("Choose a decryption method:")
        print("1. Enter shift key")
        print("2. Brute force (try all shifts)")
        decrypt_mode = int(input())
        if decrypt_mode == 1:
            shift = int(input("Enter the shift value: "))
            print("Result:", caesarCipher(text, shift, mode))
        elif decrypt_mode == 2:
            bruteForce(text)
        else:
            print("Invalid decryption method selected")
    else:
        print("Invalid option selected")

if __name__ == "__main__":
    main()
1