import random

# Predefined responses
greetings = [
    "Hello! I'm here to help. How are you feeling today?",
    "Hi there! What's on your mind?",
    "Hey! How can I support you today?"
]

responses = {
    "sad": [
        "I'm sorry you're feeling this way. Want to talk about it?",
        "That sounds hard. I'm here to listen if you want to share more.",
        "It's okay to feel sad sometimes. What can I do to help?"
    ],
    "anxious": [
        "Take a deep breath. Can you tell me what's making you anxious?",
        "I understand anxiety can be overwhelming. Let's talk about it.",
        "You're not alone. I'm here to help you through this."
    ],
    "happy": [
        "That's great to hear! What made you happy today?",
        "I'm so glad you're feeling good! Anything exciting happening?",
        "Happiness is wonderful! Share your joy with me."
    ],
    "neutral": [
        "I'm here to listen. Tell me more about how you're feeling.",
        "Let's talk about anything that's on your mind.",
        "What can I do to make your day better?"
    ]
}

crisis_response = (
    "It sounds like you might be going through a tough time. "
    "Please consider reaching out to a trusted friend or family member, "
    "or contacting a helpline. For example, in the US, you can call 988."
)

# Mood detection function
def analyze_mood(message):
    keywords = {
        "sad": ["sad", "down", "unhappy", "depressed"],
        "anxious": ["anxious", "stressed", "nervous", "worried"],
        "happy": ["happy", "joyful", "excited", "content"]
    }
    for mood, words in keywords.items():
        if any(word in message.lower() for word in words):
            return mood
    return "neutral"

# Chatbot function
def chatbot():
    print("Mental Health Chatbot: Hi! I'm here to support you. (Type 'exit' to end the chat)")
    while True:
        user_message = input("You: ").strip()
        if user_message.lower() == "exit":
            print("Mental Health Chatbot: Take care! Remember, you're not alone.")
            break

        if "suicide" in user_message.lower() or "end my life" in user_message.lower():
            print(f"Mental Health Chatbot: {crisis_response}")
            continue

        mood = analyze_mood(user_message)
        response = random.choice(responses.get(mood, responses["neutral"]))
        print(f"Mental Health Chatbot: {response}")

# Run the chatbot
if __name__ == "__main__":
    chatbot()
