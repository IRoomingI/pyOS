import data
from commands import cmd_new, cmd_dir, cmd_rm, cmd_exit

def run(user):

    commands = {
        "new": cmd_new,
        "dir": cmd_dir,
        "ls": cmd_dir,
        "rm": cmd_rm,
        "exit": cmd_exit
    }

    running = True

    while running:
        inp = input("%s/ " % data.current_dir["name"])
        invoke = inp.split(" ")[0]
        args = inp.split(" ")[1:]
        if commands.__contains__(invoke):
            commands[invoke].ex(args)
        else:
            print("This command does not exist!")
