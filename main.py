import login
import data
from run import run

def main():
    login.login()
    if run(data.user) == "logout":
        return main()


main()
