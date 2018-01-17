import data

def ex(args, user):
    if not args == "*":
        if data.make_string(args) not in data.current_dir["content"]:
            if len(args) == 1:
                if len(args) > 0:
                    args = data.make_string(args)
                    if "/" in args and not args.endswith("/"):
                        fol = args.split("/")[0]
                        dat = args.split("/")[1]
                        if fol in data.current_dir["content"]["folders"]:
                            data.current_dir["content"]["folders"][fol].append(dat)
                        else:
                            folup = {fol: []}
                            data.current_dir["content"]["folders"].update(folup)
                            data.current_dir["content"]["folders"][fol].append(dat)
                        print("successfully created file '%s' in folder '%s'" % (dat, fol))
                    elif args.endswith("/"):
                        args = args.replace("/", "")
                        args = {args: []}
                        data.current_dir["content"]["folders"].update(args)
                        args = data.make_string(args)
                        print("successfully created folder '%s/'" % args)
                    else:
                        data.current_dir["content"]["files"].append(args)
                        print("successfully created file '%s'" % args)
                else:
                    print("You must give this file a name!")
            else:
                print("Please create only one file at a time!")
        else:
            print("File already exists!")
    else:
        print("Can't create a file named *. Please choose another name!")
