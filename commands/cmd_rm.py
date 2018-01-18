import data

def ex(args, user):
    if not data.make_string(args) == "*":
        if len(args) == 1:
            args = data.make_string(args)
            if "/" in args and not args.endswith("/"):
                fol = args.split("/")[0]
                dat = args.split("/")[1]
                del data.current_dir["content"][fol][dat]
                print("successfully deleted file '%s' in folder '%s'" % (dat, fol))
            elif args.endswith("/"):
                args = args[:-1]
                if len(data.current_dir["content"]) > 0 and args in data.current_dir["content"]:
                    del data.current_dir["content"][args]
                    print("successfully deleted folder '%s/'" % args)
                else:
                    print("Please enter an existing folder name!")
            else:
                if len(data.current_dir["content"]) > 0 and args in data.current_dir["content"]:
                    del data.current_dir["content"][args]
                    print("successfully deleted file '%s'" % args)
                else:
                    print("Please enter an existing file name!")
        else:
            print("Please enter an existing file name!")
    else:
        if len(data.current_dir["content"]) > 0:
            data.current_dir["content"].clear()
        print("Removed all files and folders.")
