import login
import data
from run import run

def main():
    login.login()
    out = run(data.user)
    if out == "logout":
        return main()
    elif out == "exit":
        exit()
    elif out == "deluser":
        return main()


main()
