import login
import data
import json

def save():
    accs = login.accounts
    accs[data.user]["home"].update(data.current_dir["content"])
    data.current_dir["content"].clear
    json_acc = open("accounts.json", "w", encoding="utf-8")
    json.dump(accs, json_acc, ensure_ascii=False, indent=4)
    json_acc.close()
    login.update_accs(accs)
