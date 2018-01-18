import data

def ex(args, user):
    args = data.make_string(args)
    if args.endswith("/"):
        args = args[:-1]
        out = ""
        first = True
        if args in data.current_dir["content"]:
            for key in data.current_dir["content"][args]:
                if first:
                    out += key + "/" if data.current_dir["content"][args][key] != "*" else key
                    first = False
                else:
                    out += ", %s/" % key if data.current_dir["content"][args][key] != "*" else ", %s" % key
            print(out)
        else:
            print("Please enter an existing folder!")
    else:
        first = True
        out = ""
        for key in data.current_dir["content"]:
            if first:
                out += key + "/" if data.current_dir["content"][key] != "*" else key
                first = False
            else:
                out += ", %s/" % key if data.current_dir["content"][key] != "*" else ", %s" % key
        print(out)
