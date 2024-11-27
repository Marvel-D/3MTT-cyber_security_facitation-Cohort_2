alphabets = 'abcdefghijklmnopqrstuvwxyz'

def encrypt_caesar(num, text):
    result = ''
    for k in text.lower():
        try:
            i = (alphabets.index(k) + num) % 26
            result += alphabets[i]
        except ValueError:
            result += k
    return result.lower()

num = int(input("please input the shift:\t"))
text = input("please input the text:\t")

ciphertext = encrypt_caesar(num, text)
print("Encoded text:", ciphertext)


# # decrypt
# def decrypt_caesar(num, text):
#  results = ''
#  for k in text.lower():
#   try:
#     i = (alphabets.index(k) - num) % 26
#     results +=alphabets[i]
#   except ValueError:
#    results += k
#  return results.lower()

# num =int(input("please input the shift:\t"))
# text=input("please input the text: \t")

# # ciphertext = decrypt_caesar(num, text)
# # print("Decoded text:",ciphertext)