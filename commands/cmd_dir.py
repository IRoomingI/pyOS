import data

def ex(args, user):
    out = data.current_dir["content"].__str__().replace("'", "")
    out = out.replace("[", "")
    out = out.replace("]", "")
    print(out)
