import data

def ex(args, user):
    if args not in data.current_dir["content"]:
        if len(args) == 1:
            if len(args) > 0:
                args = data.make_string(args)
                data.current_dir["content"].append(args)
                current_dir_out = data.current_dir["content"][-1].__str__().replace("'", "")
                current_dir_out = current_dir_out.replace("[", "")
                print("successfully created file '%s'" % current_dir_out.replace("]", ""))
            else:
                print("You must give this file a name!")
        else:
            print("Please create only one file at a time!")
    else:
        print("File already exists!")
