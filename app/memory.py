import json
import os

MEMORY_FILE = "data/user_memory.json"


def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {}

    with open(MEMORY_FILE, "r") as f:
        return json.load(f)


def save_memoimport json
import os

MEMORY_FILE = "data/user_memory.json"


def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {}

    with open(MEMORY_FILE, "r") as f:
        return json.load(f)


def save_memory(memory):
    os.makedirs(os.path.dirname(MEMORY_FILE), exist_ok=True)

    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=4)


def update_user(user_id: str, key: str, value):
    memory = load_memory()

    if user_id not in memory:
        memory[user_id] = {
            "preferences": {},
            "personality": "neutral",
            "history": []
        }

    memory[user_id][key] = value

    memory[user_id]["history"].append({
        "key": key,
        "value": value
    })

    save_memory(memory)


def get_user(user_id: str):
    memory = load_memory()

    return memory.get(user_id, {
        "preferences": {},
        "personality": "neutral",
        "history": []
    })ry(memory):
    os.makedirs(os.path.dirname(MEMORY_FILE), exist_ok=True)

    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=4)


def update_user(user_id: str, key: str, value):
    memory = load_memory()

    if user_id not in memory:
        memory[user_id] = {
            "preferences": {},
            "personality": "neutral",
            "history": []
        }

    memory[user_id][key] = value

    memory[user_id]["history"].append({
        "key": key,
        "value": value
    })

    save_memory(memory)


def get_user(user_id: str):
    memory = load_memory()

    return memory.get(user_id, {
        "preferences": {},
        "personality": "neutral",
        "history": []
    })