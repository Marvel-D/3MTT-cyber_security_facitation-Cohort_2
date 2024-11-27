from cryptography.fernet import Fernet

# Generate a shared secret key
secret_key = Fernet.generate_key()
cipher = Fernet(secret_key)

print("Shared Secret Key:", secret_key.decode())

message = "Hello, Bob!".encode()

encrypted_message = cipher.encrypt(message)
print("Encrypted Message:", encrypted_message.decode())

received_encrypted_message = encrypted_message

decrypted_message = cipher.decrypt(received_encrypted_message)
print("Decrypted Message:", decrypted_message.decode())
