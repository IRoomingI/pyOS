help_info = {
    "new": " filename  - creates a new 'file'. Use 'foldername/' to create a new folder",
    "dir": "  - lists the files in your current folder",
    "ls": "  - lists the files in your current folder",
    "rm": " filename  - removes the chosen 'file' (use * to clear all files)",
    "exit": "  - exits the python script",
    "help": "  - shows you all commands",
    "logout": "  - closes the current session and asks you to log back in",
    "deluser": " true  - use this command to delete your account/user (confirm with argument: true)",
    "passwd": "  - change your password"
}


def ex(args, user):
    print("List of commands:\n")
    for key in sorted(help_info):
        print("%s%s" % (key, help_info[key]))
    print("")
