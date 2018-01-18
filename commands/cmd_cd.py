import data

def ex(args, user):
    args = data.make_string(args)
    if not args == "..":
        if data.current_dir["name"] == "home":
            if args.endswith("/") and args[:-1] in data.current_path["home"]:
                data.current_path[args[:-1]] = data.current_dir["content"][args[:-1]]
                if data.current_path["home"][args[:-1]] != "*":
                    data.set_current_dir(args[:-1])
                else:
                    print("That's not a folder!")
            else:
                print("That folder does not exist!")
        else:
            if args.endswith("/") and args[:-1] in data.current_path[data.current_dir["name"]]:
                data.current_path[args[:-1]] = data.current_dir["content"][args[:-1]]
                if data.current_path != "*":
                    del data.current_path[data.current_dir["name"]]
                    data.set_current_dir(args[:-1])
                else:
                    print("That's not a folder!")
            else:
                print("That folder does not exist!")
    else:
        if data.current_dir["name"] == "home":
            print("Can't go back further!")
        else:
            del data.current_path[data.current_dir["name"]]
            data.set_current_dir("..")
