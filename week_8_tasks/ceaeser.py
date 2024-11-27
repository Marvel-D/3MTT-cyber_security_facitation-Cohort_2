def caesar_cipher_encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isupper():
            encrypted_message += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            encrypted_message += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            encrypted_message += char
    return encrypted_message

def caesar_cipher_decrypt(encrypted_message, shift):
    decrypted_message = ""
    for char in encrypted_message:
        if char.isupper():
            decrypted_message += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            decrypted_message += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            decrypted_message += char
    return decrypted_message

# Step 1: Encrypt the message
message = "Hello 2, Bob!"
shift = 3
encrypted_message = caesar_cipher_encrypt(message, shift)
print("Encrypted Message:", encrypted_message)

# Step 2: Decrypt the message
decrypted_message = caesar_cipher_decrypt(encrypted_message, shift)
print("Decrypted Message:", decrypted_message)


# def caesar_cipher_encrypt(message, shift):
#     encrypted_message = ""
#     for char in message.lower():
#             encrypted_message += chr((ord(char) + shift) % 26)
#     return encrypted_message.lower()

# # Example
# message = "Hello, Bob!"
# shift = 3
# encrypted_message = caesar_cipher_encrypt(message, shift)
# print("Encrypted Message:", encrypted_message)

# def caesar_cipher_decrypt(encrypted_message, shift):
#     decrypted_message = ""
#     for char in encrypted_message:
#             decrypted_message += chr((ord(char) - shift) % 26)
      
#     return decrypted_message.lower()

# # Example decryption
# decrypted_message = caesar_cipher_decrypt(encrypted_message, shift)
# print("Decrypted Message:", decrypted_message)



# alphabets = 'abcdefghijklmnopqrstuvwxyz'

# def encrypt_caesar(num, text):
#  result = ' '
#  for k in text.lower():
#   try:
#     i = (alphabets.index(k) + num) % 26
#     results += alphabets[i]
#   except ValueError:
#    results+= k
#  return results.lower()
# num =int(input("please input the shift:\t"))
# text=input("please input the text: \t")
# ciphertext = encrypt_caesar(num, text)
# print("Encoded Text:", ciphertext)