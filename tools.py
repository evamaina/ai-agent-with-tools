def calculator(expression):
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Calculator error: {e}"


def save_note(note):
    try:
        with open("notes.txt", "a") as file:
            file.write(note + "\n")

        return "Note saved successfully."

    except Exception as e:
        return f"Error saving note: {e}"


def read_notes():
    try:
        with open("notes.txt", "r") as file:
            return file.read()

    except FileNotFoundError:
        return "No notes found."

    except Exception as e:
        return f"Error reading notes: {e}"