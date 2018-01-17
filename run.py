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
            if out == "logout" or out == "exit":
                accs = login.accounts
                for element in range(0, len(data.current_dir["content"]["files"])):
                    accs[user]["home_content"]["files"].append(data.current_dir["content"]["files"][element])
                    del data.current_dir["content"]["files"][element]
                for key in data.current_dir["content"]["folders"]:
                    for elem in range(0, len(data.current_dir["content"]["folders"][key])):
                        accs[user]["home_content"]["folders"][key].append(data.current_dir["content"]["folders"][key][elem])
                        del data.current_dir["content"]["folders"][key][elem]
                data.current_dir["content"]["folders"].clear
                json_acc = open("accounts.json", "w", encoding="utf-8")
                json.dump(accs, json_acc, ensure_ascii=False, indent=4)
                json_acc.close()
                login.update_accs(accs)
                running = False
            if out == "logout":
                return "logout"
            elif out == "exit":
                return "exit"
            elif out == "deluser":
                return "deluser"

        else:
            print("This command does not exist!")
