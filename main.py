from openai import OpenAI
from dotenv import load_dotenv
from tools import run_tool
from agent.prompts import AGENT_PROMPT

load_dotenv()

client = OpenAI()


def ask_ai(user_message):

    prompt = AGENT_PROMPT.format(user_message=user_message)

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

    while True:
        user_message = input("\nYou: ")

        if user_message.lower() == "exit":
            print("Goodbye!")
            break

        answer = ask_ai(user_message)

        print(f"\nAgent: {answer}")


if __name__ == "__main__":
    main()