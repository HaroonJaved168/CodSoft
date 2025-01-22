# Simple chatbot with predefined rules

def chatbot_response(user_input):
    # Predefined responses
    responses = {
        "hello": "Hi there! How can I assist you today?",
        "how are you": "I'm just a bot, but I'm doing great! How about you?",
        "what is your name": "I'm ChatBot, your virtual assistant!",
        "bye": "Goodbye! Have a great day!",
        "help": "Sure, I can help! Ask me anything.",
    }

    # Normalize user input to lowercase for matching
    user_input = user_input.lower()

    # Check if the user input matches any predefined response
    if user_input in responses:
        return responses[user_input]
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"

# Main loop to interact with the chatbot
def main():
    print("ChatBot: Hello! I'm your assistant. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("ChatBot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print(f"ChatBot: {response}")

if __name__ == "__main__":
    main()
