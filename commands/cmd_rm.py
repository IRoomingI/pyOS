import data

def ex(args, user):
    args = data.make_string(args)
    if len(args) > 0 and len(data.current_dir["content"]) > 0 and args in data.current_dir["content"]:
        index = data.current_dir["content"].index(args)
        current_dir_out = data.current_dir["content"][index].__str__().replace("'", "")
        data.current_dir["content"].remove(args)
        current_dir_out = current_dir_out.replace("[", "")
        print("successfully deleted file '%s'" % current_dir_out.replace("]", ""))
    else:
        print("You must enter an existing file name!")
