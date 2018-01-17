import data
import login
import json


def run(user):

    running = True

    while running:
        inp = input("%s/ " % data.current_dir["name"])
        invoke = inp.split(" ")[0]
        args = inp.split(" ")[1:]
        if data.commands.__contains__(invoke):
            out = data.commands[invoke].ex(args=args, user=user)
            if out == "logout":
                accs = login.accounts
                for element in range(0, len(data.current_dir["content"])):
                    accs[user]["home_content"]["files"].append(data.current_dir["content"][element])
                    print("appended %s" % element)
                json_acc = open("accounts.json", "w", encoding="utf-8")
                json.dump(accs, json_acc, ensure_ascii=False)
                json_acc.close()
                login.update_accs(accs)
                running = False
                return "logout"
        else:
            print("This command does not exist!")
