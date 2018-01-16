import data

def ex(args):
    if args not in data.current_dir["content"]:
        if len(args) > 0:
            data.current_dir["content"].append(args)
            current_dir_out = data.current_dir["content"][-1].__str__().replace("'", "")
            current_dir_out = current_dir_out.replace("[", "")
            print("successfully created file '%s'" % current_dir_out.replace("]", ""))
        else:
            print("You must give this file a name!")
    else:
        print("File already exists!")
