import json
import os
os.makedirs("users", exist_ok=True)
def save_user(username, password):

    user_file = f"users/{username}.json"

    data = {
        "username": username,
        "password": password
    }

    with open(user_file, "w") as f:
        json.dump(data, f)
def user_exists(username):

    return os.path.exists(
        f"users/{username}.json"
    )
def verify_user(username, password):

    file = f"users/{username}.json"

    if not os.path.exists(file):
        return False

    with open(file, "r") as f:
        data = json.load(f)

    return data["password"] == password