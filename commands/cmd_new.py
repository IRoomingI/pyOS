import data

def ex(args, user):
    if not args == "*":
        if data.make_string(args) not in data.current_dir["content"]:
            if len(args) == 1:
                if len(args) > 0:
                    args = data.make_string(args)
                    path = data.current_dir["content"]
                    if "/" in args and not args.endswith("/"):
                        fol = args.split("/")[0]
                        dat = args.split("/")[1]
                        if fol in path:
                            path.update({fol: {dat: "*"}})
                        else:
                            folup = {fol: {dat: "*"}}
                            path.update(folup)
                        print("successfully created file '%s' in folder '%s'" % (dat, fol))
                    elif args.endswith("/"):
                        args = args[:-1]
                        args = {args: {}}
                        path.update(args)
                        print("successfully created folder '%s/'" % data.make_string(args))
                    else:
                        args = {args: "*"}
                        path.update(args)
                        print("successfully created file '%s'" % data.make_string(args).replace("*", ""))
                else:
                    print("You must give this file a name!")
            else:
                print("Please create only one file at a time!")
        else:
            print("File already exists!")
    else:
        print("Can't create a file named *. Please choose another name!")
