#welcome to our chatbot
import random
import nltk
from patterns import pattern
from talk import listen


nltk.download('punkt')

patterns = pattern()

resources = {
    "anxiety": "https://www.nimh.nih.gov/health/topics/anxiety-disorders",
    "depression": "https://www.mentalhealth.gov/your-mental-health/depression",
    "coping mechanisms": "https://www.helpguide.org/articles/mental-health/coping-with-stress.htm",
    "professional help": "https://www.mentalhealth.gov/get-help"
}


def respond(user_input):
    # Preprocess user input (e.g., lowercase, tokenize)
    processed_input = nltk.word_tokenize(user_input.lower())
    # Find the best matching pattern
    for pattern in patterns:
        for keyword in pattern["pattern"].split():
            if keyword.lower() in processed_input:
                # Choose a random response from the matched pattern
                return random.choice(pattern["responses"])
    # No matching pattern found, offer a default response
    return "I'm still learning, but I couldn't understand your request. Try asking something else or saying 'help'."


# Example usage
while True:
    user_input = listen()
    bot_response = respond(user_input)
    print("Chatbot:", bot_response)
