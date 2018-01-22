import data as dat
import json
from appJar import gui

app = gui("pyOS Login", "360x250")

json_acc = open("accounts.json", "r", encoding="utf-8")
accounts = json.load(json_acc)
json_acc.close()

def update_accs(accs):
    global accounts
    accounts = accs

def cancel(button):
    if button == "Cancel":
        dat.user = "*"
        app.stop()

def press(button):
    if app.getRadioButton("select") == "Login":
        dat.user = app.getEntry("Username")
        pwd = app.getEntry("Password")
        if check_user():
            if check_passwd(pwd):
                app.stop()
    elif app.getRadioButton("select") == "Register":
        dat.user = app.getEntry("Username")
        register()


def select(radioButton):
    if app.getRadioButton("select") == "Login":
        app.showLabel("l3")
        app.hideLabel("l4")
        app.hideEntry("Repeat Password")
    if app.getRadioButton("select") == "Register":
        app.showLabel("l4")
        app.showEntry("Repeat Password")

def check_passwd(passwd):
    if passwd == accounts[dat.user]["passwd"]:
        return True
    else:
        app.errorBox("Login Error", "The password you entered was not correct!")
        return False

def check_user():
    if len(accounts) > 0:
        if dat.user in accounts:
            dat.set_accs(accounts)
            dat.set_user(dat.user)
            return True
        else:
            app.errorBox("Login Error", "The username you entered does not exist!")
            return False
    else:
        app.infoBox("No users!", "There are no accounts yet. Please register a new user!")
        return False

def register():
    if dat.user in accounts:
        app.errorBox("Username Error", "Username already exists! Please choose another name.")
    else:
        dat.set_user(dat.user)
        passwd = app.getEntry("Password")
        check_passwd = app.getEntry("Repeat Password")
        if not passwd == "":
            if passwd == check_passwd:
                data = {dat.user: {"passwd": passwd, "home": {}}}
                accounts.update(data)
                dat.set_accs(accounts)
                json_acc = open("accounts.json", "w", encoding="utf-8")
                json.dump(accounts, json_acc, ensure_ascii=False, indent=4)
                json_acc.close()
                app.stop()
                print("Hello %s, your login was successfull." % dat.user.capitalize())
            else:
                app.errorBox("Password Error", "Passwords aren't matching! Please try again.")
        else:
            app.errorBox("Password Error", "You can't leave your password blank! Please enter something.")


def setup():
        app.setBg("RoyalBlue1")
        app.setSticky("")
        app.setExpand("both")

        app.addLabel("title", "pyOS Login Screen", colspan=2)
        app.setLabelBg("title", "white")

        app.addRadioButton("select", "Login", 1, 0)
        app.addRadioButton("select", "Register", 1, 1)
        app.setRadioButtonChangeFunction("select", select)

        app.addLabel("l2", "Username", 2, 0)
        app.addEntry("Username", 2, 1)

        app.addLabel("l3", "Password", 3, 0)
        app.addSecretEntry("Password", 3, 1)

        app.addLabel("l4", "Repeat Password", 4, 0)
        app.addSecretEntry("Repeat Password", 4, 1)

        app.setRadioButton("select", "Login", callFunction=True)
        app.addButton("Submit", press, 5, 0)
        app.addButton("Cancel", cancel, 5, 1)

        app.go()
