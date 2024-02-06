from cryptography.fernet import Fernet


def Load_Key():
    with open("dataStorage/key.key", "rb") as key_file:
        key = key_file.read()
    return key


token = Fernet(Load_Key())


def View():
    with open("dataStorage/password.txt", 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, password = data.split('|')
            print("User: ", user, ", Password:",
                  token.decrypt(password.encode()).decode())


def Add():
    name = input("enter your name: ")
    new_password = input("enter your password: ")

    with open("dataStorage/password.txt", 'a') as f:
        f.write(name + '|' + token.encrypt(new_password.encode()).decode() + "\n")


while True:
    mode = input("would you like to do (add, view or quit): ")
    if mode == "quit":
        break
    if mode == "view":
        View()
    if mode == "add":
        Add()
