from cryptography.fernet import Fernet


def Load_key():
    with open("dataStorage/key.key", "rb") as key_file:
        key = key_file.read()
    return key


f = Fernet(Load_key())

token = f.encrypt(b"my deep dark secret")
decrypted_token = f.decrypt(token)

print(Load_key())
print(token)
print(decrypted_token)
