from openai import OpenAI
from dotenv import load_dotenv
from tools import calculator, save_note, read_notes

load_dotenv()

client = OpenAI()


def ask_ai(user_message):
    prompt = f"""
    You are an AI agent.

    Available tools:

    calculator:
    Use for math.

    save_note:
    Use when user wants to remember, save, store or note something.

    read_notes:
    Use when user asks what has been saved before.

    Rules:

    For calculator:

    TOOL: calculator
    INPUT: expression

    For save_note:

    TOOL: save_note
    INPUT: note content

    For read_notes:

    TOOL: read_notes
    INPUT: none

    Otherwise answer normally.

    User message:
    {user_message}
    """

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    ai_response = response.output_text.strip()

    tool_result = None

    if ai_response.startswith("TOOL: calculator"):
        expression = ai_response.split("INPUT:")[1].strip()
        tool_result = calculator(expression)

    elif ai_response.startswith("TOOL: save_note"):
        note = ai_response.split("INPUT:")[1].strip()
        tool_result = save_note(note)

    elif ai_response.startswith("TOOL: read_notes"):
        tool_result = read_notes()

    if tool_result is not None:
        final_prompt = f"""
    User request:
    {user_message}

    Tool output:
    {tool_result}

    Create the final response.
    """

        final_response = client.responses.create(
            model="gpt-4.1-mini",
            input=final_prompt
        )

        return final_response.output_text

    return ai_response


def main():
    print("AI Agent started. Type 'exit' to quit.")

    while True:
        user_message = input("\nYou: ")

        if user_message.lower() == "exit":
            print("Goodbye!")
            break

        answer = ask_ai(user_message)
        print(f"\nAgent: {answer}")


if __name__ == "__main__":
    main()