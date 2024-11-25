from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Load helpful responses
greetings = [
    "Hello! I'm here to support you. How are you feeling today?",
    "Hi! I'm glad you reached out. What's on your mind?",
    "Hey there! How can I help you today?"
]

responses = {
    "sad": [
        "I'm sorry to hear that. Want to share more about what's making you feel this way?",
        "That sounds tough. Remember, it's okay to feel this way sometimes. I'm here to listen.",
        "I'm here for you. What can we do together to make things a bit better?"
    ],
    "anxious": [
        "Take a deep breath. Can you tell me what's making you feel this way?",
        "Anxiety can be overwhelming. How about we talk it through together?",
        "You're not alone in this. I'm here to help. What's on your mind?"
    ],
    "happy": [
        "That's wonderful to hear! What made you feel this way?",
        "I'm so glad you're feeling good! Let's celebrate the positive moments.",
        "Keep that positive energy going! Anything exciting happening today?"
    ]
}

crisis_response = (
    "I'm not a professional, but it sounds like you might be in crisis. "
    "Please reach out to a trusted friend, family member, or call a helpline in your area. "
    "For example, you can call 988 (in the US) or search for a local hotline."
)


def analyze_mood(message):
    keywords = {
        "sad": ["sad", "unhappy", "depressed", "down"],
        "anxious": ["anxious", "worried", "stressed", "nervous"],
        "happy": ["happy", "joyful", "excited", "content"]
    }

    for mood, words in keywords.items():
        if any(word in message.lower() for word in words):
            return mood
    return "neutral"


@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    if not user_message:
        return jsonify({"response": "Can you please share more? I'm here to help."})

    mood = analyze_mood(user_message)

    if "suicide" in user_message.lower() or "end my life" in user_message.lower():
        return jsonify({"response": crisis_response})

    if mood in responses:
        return jsonify({"response": random.choice(responses[mood])})

    return jsonify({"response": random.choice(greetings)})


@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Mental Health Chatbot API!"


if __name__ == "__main__":
    app.run(debug=True)
