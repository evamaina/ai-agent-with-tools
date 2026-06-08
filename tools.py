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


def read_notes(_input=None):
    try:
        with open("notes.txt", "r") as file:
            return file.read()
    except FileNotFoundError:
        return "No notes found."
    except Exception as e:
        return f"Error reading notes: {e}"
    

def read_file(filename):
    try:
        with open(filename, "r") as file:
            return file.read()

    except FileNotFoundError:
        return "File not found."

    except Exception as e:
        return f"Error reading file: {e}"


TOOLS = {
    "calculator": calculator,
    "save_note": save_note,
    "read_notes": read_notes,
    "read_file": read_file,
}


def run_tool(tool_name, tool_input):
    tool = TOOLS.get(tool_name)

    if tool is None:
        return f"Tool '{tool_name}' not found."

    return tool(tool_input)