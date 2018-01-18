from commands import cmd_new, cmd_dir, cmd_rm, cmd_exit, cmd_help, cmd_logout, cmd_deluser, cmd_passwd, cmd_cd

commands = {
    "new": cmd_new,
    "dir": cmd_dir,
    "ls": cmd_dir,
    "rm": cmd_rm,
    "exit": cmd_exit,
    "help": cmd_help,
    "logout": cmd_logout,
    "deluser": cmd_deluser,
    "passwd": cmd_passwd,
    "cd": cmd_cd
}

user = ""

def make_string(var):
    if type(var) == list:
        var = var.__str__().replace("[", "")
        var = var.replace("]", "")
    elif type(var) == dict:
        var = var.__str__().replace("[", "")
        var = var.replace("]", "")
        var = var.replace("{", "")
        var = var.replace("}", "")
        var = var.replace(":", "")
        var = var.replace(" ", "")
    var = var.replace("'", "")
    return var


def set_user(value):
    global user
    user = value


current_dir = {}
current_path = {}

accs = None
def set_accs(dic):
    global accs, current_dir, user, current_path
    accs = dic
    current_dir = {"name": "home", "content": dic[user]["home"]}
    current_path = accs[user].copy()
    del current_path["passwd"]


def set_current_dir(value):
    global current_dir, current_path
    if current_path != "*":
        if current_dir["name"] == "home":
            current_dir["name"] = value
            current_dir["content"] = current_path["home"][value]
            print(current_path)
            # del current_path["home"]
        elif value == "..":
            current_dir["content"] = current_path[next(iter(current_path))]
            current_dir["name"] = next(iter(current_path))
            print(current_path)
            print(current_dir)
        else:
            print(current_path)
            current_dir["name"] = value
            current_dir["content"] = current_path[current_dir["name"]]
            print(current_path)
