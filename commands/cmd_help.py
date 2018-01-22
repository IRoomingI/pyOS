help_info = {
    "new": " filename  - creates a new 'file'. Use 'foldername/' to create a new folder",
    "dir": "  - lists files and folders in the chosen folder",
    "ls": "  - lists files and folders in the chosen folder",
    "rm": " filename  - removes the chosen 'file'. Use 'foldername/' to delete a folder",
    "exit": "  - closes the current session",
    "help": "  - shows all commands to you",
    "logout": "  - closes the current session",
    "deluser": " true  - use this command to delete your account/user (confirm with argument: true)",
    "passwd": "  - change your password",
    "cd": "  - change your current folder (type: 'cd ..' to get back to your home folder)"
}


def ex(args, user):
    print("List of commands:\n")
    for key in sorted(help_info):
        print("%s%s" % (key, help_info[key]))
    print("")
