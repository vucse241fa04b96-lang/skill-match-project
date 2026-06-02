import json
import os

def save_chat(chat_file, messages):

    with open(chat_file, "w") as f:
        json.dump(messages, f, indent=4)

def load_chat(chat_file):

    try:
        with open(chat_file, "r") as f:
            return json.load(f)

    except:
        return []

import os

def get_user_chats(username):

    user_folder = f"chats/{username}"

    if not os.path.exists(user_folder):
        return []

    return sorted(
        os.listdir(user_folder),
        reverse=True
    )
##
def get_chat_title(chat_file):

    data = load_chat(chat_file)

    if len(data) > 0:
        return data[0]["content"][:40]

    return "New Chat"