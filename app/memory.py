import json
import os

MEMORY_FILE = "data/user_memory.json"


# -----------------------------
# LOAD USER MEMORY
# -----------------------------
def get_user(user_id: str):
    if not os.path.exists(MEMORY_FILE):
        return {}

    with open(MEMORY_FILE, "r") as f:
        data = json.load(f)

    return data.get(user_id, {})


# -----------------------------
# UPDATE USER MEMORY
# -----------------------------
def update_user(user_id: str, new_data: dict):
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            data = json.load(f)
    else:
        data = {}

    data[user_id] = new_data

    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=2)


# -----------------------------
# SAVE MEMORY (alias safe)
# -----------------------------
def save_memory(user_id: str, new_data: dict):
    update_user(user_id, new_data)