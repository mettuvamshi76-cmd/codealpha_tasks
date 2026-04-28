def reply(user_text):
    # simple rule-based responses
    if user_text in ["hello", "hi", "hey"]:
        return "Hi there!"
    
    elif user_text == "how are you":
        return "I'm doing good, thanks for asking!"
    
    elif user_text == "what is your name":
        return "I'm a simple Python chatbot."
    
    elif user_text == "bye":
        return "Goodbye! Have a nice day!"
    
    else:
        return "Sorry, I didn't understand that."

def start_chat():
    print("🤖 Chatbot started (type 'bye' to exit)\n")

    while True:
        user_input = input("You: ").lower()

        response = reply(user_input)
        print("Bot:", response)

        if user_input == "bye":
            break

# run chatbot
start_chat()
