import login
import data
from save import save
from run import run

def main():
    login.login()
    out = run(data.user)
    if out == "logout":
        save()
        return main()
    elif out == "exit":
        save()
        exit()
    elif out == "deluser":
        return main()


main()
