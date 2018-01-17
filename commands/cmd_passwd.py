from getpass import getpass
import login

def ex(args, user):
    passwd_cur = getpass("Enter your current password: ")
    if passwd_cur == login.accounts[user]["passwd"]:
        passwd = getpass("New password:")
        passwd_conf = getpass("Repeat password: ")
        if passwd == passwd_conf:
            login.accounts[user]["passwd"] = passwd
    else:
        print("Password was incorrect, please try again!")
