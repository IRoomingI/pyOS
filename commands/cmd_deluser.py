import json
import login

def ex(args, user):
    if len(args) == 1:
        args = args.__str__().replace("[", "")
        args = args.replace("]", "")
        args = args.replace("'", "")
        print(args)
        if args == "true":
            json_acc = open("accounts.json", "r", encoding="utf-8")
            accounts = json.load(json_acc)
            json_acc.close()
            del accounts[user]
            login.update_accs(accounts)
            json_acc = open("accounts.json", "w", encoding="utf-8")
            json.dump(accounts, json_acc, ensure_ascii=False)
            json_acc.close()
            print("Deleted user!")
            return "logout"
        else:
            print("Please type 'deluser true' to delete your account")
    else:
        print("Please type 'deluser true' to delete your account")
