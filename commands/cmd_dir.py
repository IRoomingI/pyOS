import data

def ex(args):
    out = data.current_dir["content"].__str__().replace("'", "")
    out = out.replace("[", "")
    out = out.replace("]", "")
    print(out)
