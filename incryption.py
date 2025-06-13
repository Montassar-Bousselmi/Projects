import random
import string

def input_fn():
    print("Welcome to the Incryption Program! \n")
    print("1. Generate a new key \n")
    print("2. Encrypt a message \n")
    print("3. Decrypt a message \n")
    print("4. Exit \n")
    while True:
        choice=int(input("Enter your choice: "))
        if choice in [1, 2, 3, 4]:
            break
        else:
            print("Invalid choice. Please try again.\n")
    return choice


def each_char_is_unique(s):
    return len(s) == len(set(s))

def verify_key(key):
    if len(key)!= 73 :
        return False
    if not each_char_is_unique(key):
        return False
    else:
        return True

def generate_key():
    key=""
    for i in range(73):
        char=chr(random.randint(33, 126))
        while char in key:
            char=chr(random.randint(33, 126))
        key+=char
    return key

def encrypt(message,key):
    if not verify_key(key):
        return "Invalid key"
    encrypted_message = ""
    test="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789"
    for char in message:
        if char in test:
            index = test.index(char)
            encrypted_message += key[index]
        else:
            encrypted_message += char
    return encrypted_message


def decrypt(encrypted_message,key):
    if not verify_key(key):
        return "Invalid key"
    decrypted_message = ""
    test="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789"
    for char in encrypted_message:
        if char in key:
            index=key.index(char)
            decrypted_message += test[index]
        else:
            decrypted_message += char
    return decrypted_message

def main():
    choice= input_fn()
    while choice != 4:
        if choice == 1:
            key= generate_key()
            print(f"Generated Key: {key}\n")
        elif choice == 2:
            key= input("Enter the key: ")
            message= input("Enter the message to encrypt: ")
            encrypted_message = encrypt(message, key)
            print(f"Encrypted Message: {encrypted_message}\n")
        elif choice == 3:
            key= input("Enter the key: ")
            encrypted_message = input("Enter the message to decrypt: ")
            decrypted_message = decrypt(encrypted_message, key)
            print(f"Decrypted Message: {decrypted_message}\n")
        choice = input_fn()
        if choice == 4:
            print("Exiting the program. Goodbye!")
            break
main()