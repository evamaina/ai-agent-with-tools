from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()


def ask_ai(user_message):
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=user_message
    )

    return response.output_text


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