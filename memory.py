import json

MEMORY_FILE = "conversation_history.json"


def load_conversation_history():
    try:
        with open(MEMORY_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_conversation_history(conversation_history):
    with open(MEMORY_FILE, "w") as file:
        json.dump(conversation_history, file, indent=4)