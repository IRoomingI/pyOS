from commands import cmd_new, cmd_dir, cmd_rm, cmd_exit, cmd_help, cmd_logout, cmd_deluser, cmd_passwd

commands = {
    "new": cmd_new,
    "dir": cmd_dir,
    "ls": cmd_dir,
    "rm": cmd_rm,
    "exit": cmd_exit,
    "help": cmd_help,
    "logout": cmd_logout,
    "deluser": cmd_deluser,
    "passwd": cmd_passwd
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
    set_current_dir(user)


current_dir = {"name": user, "content": {"files": [], "folders": {}}}

accs = None
def set_accs(dic):
    global accs, current_dir, user
    accs = dic
    current_dir = {"name": user, "content": {"files": accs[user]["home_content"]["files"], "folders": accs[user]["home_content"]["folders"]}}


def set_current_dir(value):
    global current_dir
    current_dir["name"] = value
