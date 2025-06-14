def chatbot():
    print("Welcome! Let's chat.")
    print("You can say: hello, how are you, bye")
    print("Type 'exit' to end the chat.\n")

    while True:
        message = input("You: ").lower()

        if message == "hello":
            print("Bot: Hi!")
        elif message == "how are you":
            print("Bot: I'm fine, thanks!")
        elif message == "bye":
            print("Bot: Goodbye!")
        elif message == "exit":
            print("Bot: Chat closed.")
            break
        else:
            print("Bot: Sorry, I didn't understand that.")

# Start the chatbot
chatbot()
