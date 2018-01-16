import data
import json
from getpass import getpass

json_acc = open("accounts.json", "r", encoding="utf-8")
accounts = json.load(json_acc)
json_acc.close()

def check_passwd(passwd):
    if passwd == accounts[data.user]:
        return True
    else:
        return False

def check_user():
    if data.user in accounts:
        return True
    else:
        return False

def register():
    name = input("Enter a username: ")
    if name in accounts:
        print("User already exists!")
        return register()
    passwd = getpass("New password: ")
    check_passwd = getpass("Reapeat password: ")
    if passwd == check_passwd:
        data = {name: passwd}
        accounts.update(data)
        json_acc = open("accounts.json", "w", encoding="utf-8")
        json.dump(accounts, json_acc, ensure_ascii=False)
        json_acc.close()
        return login()

def login():
    data.set_user(input("Please enter your username: "))
    if check_user():
        passwd = getpass()
        if check_passwd(passwd):
            print("Hello %s, your login was successfull." % data.user.capitalize())
        else:
            print("Incorrect password, please try again.\n")
            return login()
    else:
        out = input("Username does not exist!\nTry again (y) or create new account (n)? ")
        if out == "n" or out == "N":
            register()
        elif out == "j" or out == "J":
            login()
        else:
            print("Invalid input!\n")
            login()
