import data

def ex(args, user):
    args = data.make_string(args)
    if args.endswith("/"):
        args = args[:-1]
        if args in data.current_dir["content"]["folders"]:
            out = data.make_string(data.current_dir["content"]["folders"][args])
            print(out)
        else:
            print("Please enter an existing folder!")
    else:
        out = data.make_string(data.current_dir["content"]["files"])
        first = True
        for key in data.current_dir["content"]["folders"]:
            if first and len(data.current_dir["content"]["files"]) == 0:
                out += key + "/"
                first = False
            else:
                out += ", %s/" % key
        print(out)
