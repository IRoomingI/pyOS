import data as dat
import json
from getpass import getpass

json_acc = open("accounts.json", "r", encoding="utf-8")
accounts = json.load(json_acc)
json_acc.close()

def update_accs(accs):
    global accounts
    accounts = accs

def check_passwd(passwd):
    if passwd == accounts[dat.user]["passwd"]:
        print("Hello %s, your login was successfull." % dat.user.capitalize())
        return True
    else:
        return False

def check_user():
    if len(accounts) > 0:
        dat.set_user(input("Please enter your username: "))
        dat.set_accs(accounts)
        if dat.user in accounts:
            return True
        else:
            print("Username does not exist!")
            return False
    else:
        print("Please create a new user!")
        return False

def register():
    name = input("Enter a username: ")
    if name in accounts:
        print("User already exists!")
        return register()
    dat.set_user(name)
    passwd = getpass("New password: ")
    check_passwd = getpass("Reapeat password: ")
    if passwd == check_passwd:
        data = {name: passwd}
        accounts.update(data)
        json_acc = open("accounts.json", "w", encoding="utf-8")
        json.dump(accounts, json_acc, ensure_ascii=False)
        json_acc.close()
        print("Hello %s, your login was successfull." % dat.user.capitalize())
    else:
        print("Passwords aren't matching! Please try again.")
        return register()

def login():
    if check_user():
        passwd = getpass()
        if not check_passwd(passwd):
            print("Incorrect password, please try again.\n")
            return login()
    else:
        if len(accounts) > 0:
            out = input("Try again (y) or create new account (n)? ")
            if out.lower() == "n":
                register()
            elif out.lower() == "y":
                login()
            else:
                print("Invalid input!\n")
                login()
        else:
            register()
