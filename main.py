import login
import data
from save import save
from run import run

def main():
    login.setup()
    if data.user != "*":
        out = run(data.user)
        if out == "logout":
            save()
            exit()
        elif out == "exit":
            save()
            exit()
        elif out == "deluser":
            save()
            exit()
    else:
        exit()


main()
