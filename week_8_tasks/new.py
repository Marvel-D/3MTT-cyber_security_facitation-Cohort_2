import_file = "task.txt"

alphabets = 'abcdefghijklmnopqrstuvwxyz'

with open(import_file, "r") as file:
    fileList = file.read()
# fileList = fileList.split()

print(fileList)

def encrypt_caesar(num):
    result = ''
    for k in fileList.lower():
        try:
            i = (alphabets.index(k) + num) % 26
            result += alphabets[i]
        except ValueError:
            result += k
    return result.lower()

num = int(input("please input the shift:\t"))
# text = input("please input the text:\t")

ciphertext = encrypt_caesar(num)
print("Encoded text:", ciphertext)
