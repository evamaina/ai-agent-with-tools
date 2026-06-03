from openai import OpenAI
from dotenv import load_dotenv
from tools import calculator

load_dotenv()

client = OpenAI()


def ask_ai(user_message):
    prompt = f"""
You are an AI agent.

You can either:
1. Answer normally
2. Use the calculator tool

If the user asks for math, respond exactly like this:
TOOL: calculator
INPUT: the math expression only

User message: {user_message}
"""

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    ai_response = response.output_text.strip()

    if ai_response.startswith("TOOL: calculator"):
        expression = ai_response.split("INPUT:")[1].strip()
        tool_result = calculator(expression)

        final_prompt = f"""
The user asked: {user_message}

The calculator result is: {tool_result}

Give the final answer to the user clearly.
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