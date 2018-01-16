user = ""

def set_user(value):
    global user
    user = value
    set_current_dir(user)


current_dir = {"name": "", "content": []}

def set_current_dir(value):
    global current_dir
    current_dir["name"] = value
