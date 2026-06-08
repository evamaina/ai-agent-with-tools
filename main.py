from openai import OpenAI
from dotenv import load_dotenv
from tools import run_tool
from agent.prompts import AGENT_PROMPT
from memory import load_conversation_history, save_conversation_history

load_dotenv()

client = OpenAI()


def format_history(conversation_history):
    if not conversation_history:
        return "No previous conversation."

    formatted = ""

    for message in conversation_history:
        role = message["role"]
        content = message["content"]
        formatted += f"{role}: {content}\n"

    return formatted


def ask_ai(user_message, conversation_history):
    history_text = format_history(conversation_history)

    prompt = AGENT_PROMPT.format(
        user_message=user_message,
        conversation_history=history_text
    )

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    ai_response = response.output_text.strip()

    if ai_response.startswith("TOOL:"):
        lines = ai_response.splitlines()

        tool_name = lines[0].replace("TOOL:", "").strip()
        tool_input = lines[1].replace("INPUT:", "").strip()

        tool_result = run_tool(tool_name, tool_input)

        final_prompt = f"""
Previous conversation:
{history_text}

User request:
{user_message}

Tool used:
{tool_name}

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

    conversation_history = load_conversation_history()

    while True:
        user_message = input("\nYou: ")

        if user_message.lower() == "exit":
            print("Goodbye!")
            break

        answer = ask_ai(user_message, conversation_history)

        conversation_history.append({
            "role": "user",
            "content": user_message
        })

        conversation_history.append({
            "role": "agent",
            "content": answer
        })
        
        save_conversation_history(conversation_history)

        print(f"\nAgent: {answer}")


if __name__ == "__main__":
    main()