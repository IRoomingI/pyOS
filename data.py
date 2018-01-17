from commands import cmd_new, cmd_dir, cmd_rm, cmd_exit, cmd_help, cmd_logout, cmd_deluser

user = ""

def make_string(var):
    var = var.__str__().replace("[", "")
    var = var.replace("]", "")
    var = var.replace("'", "")
    return var


def set_user(value):
    global user
    user = value
    set_current_dir(user)


current_dir = {"name": user, "content": None}

accs = None
def set_accs(dic):
    global accs, current_dir, user
    accs = dic
    current_dir = {"name": user, "content": accs[user]["home_content"]["files"]}


def set_current_dir(value):
    global current_dir
    current_dir["name"] = value


commands = {
    "new": cmd_new,
    "dir": cmd_dir,
    "ls": cmd_dir,
    "rm": cmd_rm,
    "exit": cmd_exit,
    "help": cmd_help,
    "logout": cmd_logout,
    "deluser": cmd_deluser
}
