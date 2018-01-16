import data

def ex(args):
    if len(args) > 0 and len(data.current_dir["content"]) > 0:
        str(args)
        index = data.current_dir["content"].index(args)
        current_dir_out = data.current_dir["content"][index].__str__().replace("'", "")
        data.current_dir["content"].remove(args)
        current_dir_out = current_dir_out.replace("[", "")
        print("successfully deleted file '%s'" % current_dir_out.replace("]", ""))
    else:
        print("You must enter an existing file name!")
