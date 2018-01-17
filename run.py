import data


def run(user):

    running = True

    while running:
        inp = input("%s/ " % data.current_dir["name"])
        invoke = inp.split(" ")[0]
        args = inp.split(" ")[1:]
        if invoke in data.commands:
            out = data.commands[invoke].ex(args=args, user=user)
            if type(out) is str:
                # accs = login.accounts
                # for element in range(0, len(data.current_dir["content"]["files"])):
                #     accs[user]["home_content"]["files"].append(data.current_dir["content"]["files"][element])
                #     del data.current_dir["content"]["files"][element]
                # for key in data.current_dir["content"]["folders"]:
                #     for elem in range(0, len(data.current_dir["content"]["folders"][key])):
                #         accs[user]["home_content"]["folders"][key].append(data.current_dir["content"]["folders"][key][elem])
                #         del data.current_dir["content"]["folders"][key][elem]
                # data.current_dir["content"]["folders"].clear
                # json_acc = open("accounts.json", "w", encoding="utf-8")
                # json.dump(accs, json_acc, ensure_ascii=False, indent=4)
                # json_acc.close()
                # login.update_accs(accs)
                running = False
                return out
        else:
            print("This command does not exist!")
