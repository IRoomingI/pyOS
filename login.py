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
    name = input("Wie soll dein Benutzername lauten? ")
    if name in accounts:
        print("Benutzer existiert bereits!")
        return register()
    passwd = getpass("Neues Passwort: ")
    check_passwd = getpass("Passwort Wiederholen: ")
    if passwd == check_passwd:
        data = {name: passwd}
        accounts.update(data)
        json_acc = open("accounts.json", "w", encoding="utf-8")
        json.dump(accounts, json_acc, ensure_ascii=False)
        json_acc.close()
        return login()

def login():
    data.set_user(input("Bitte gib deinen Benutzernamen an: "))
    if check_user():
        passwd = getpass("Passwort: ")
        if check_passwd(passwd):
            print("Hallo %s, du wurdest erfolgreich eingeloggt." % data.user.capitalize())
        else:
            print("Passwort nicht korrekt, bitte versuche es erneut.\n")
            return login()
    else:
        out = input("Benutzername existiert nicht!\nErneut versuchen (j) oder neuen Account erstellen (n)? ")
        if out == "n" or out == "N":
            register()
        elif out == "j" or out == "J":
            login()
        else:
            print("Keine gültige Eingabe!\n")
            login()
