from  app.gemini.geminiclient import get_gemini_client 

def main():
    client = get_gemini_client()
    print("Welcome to Gemini AI Terminal Interface! Type 'exit' to quit.")

    while True:
        user_input = input("\nEnter your prompt: ")
        if user_input.strip().lower() == "exit":
            print("Exiting... Goodbye!")
            break

        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=user_input
            )
            print("\nAI Response:\n" + response.text)
        except Exception as e:
            print(f"Error generating response: {e}")

if __name__ == "__main__":
    main()
