import data


def run(user):

    running = True

    while running:
        inp = input("%s/ " % data.current_dir["name"])
        invoke = inp.split(" ")[0]
        args = inp.split(" ")[1:]
        if invoke in data.commands:
            out = data.commands[invoke].ex(args=args, user=user)
            if type(out) is str:
                running = False
                return out
        else:
            print("This command does not exist!")
