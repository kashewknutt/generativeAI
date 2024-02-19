#welcome to our chatbot
import random
import nltk
from patterns import pattern
from talk import listen
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline


nltk.download('punkt')

patterns = pattern()

def train_classifier(training_data):
    texts = [example["pattern"] for example in training_data]
    labels = [example["responses"] for example in training_data]
    model = make_pipeline(CountVectorizer(), MultinomialNB())
    model.fit(texts, labels)
    return model


def respond(user_input, model):
    # Preprocess user input (e.g., lowercase, tokenize)
    processed_input = nltk.word_tokenize(user_input.lower())
    predicted_label = model.predict([user_input.lower()])[0]
    # Find the best matching pattern
    for pattern in patterns:
        for keyword in pattern["pattern"].split():
            if keyword.lower() in processed_input:
                # Choose a random response from the matched pattern
                return random.choice(pattern["responses"])
    # No matching pattern found, offer a default response
    return "I'm still learning, but I couldn't understand your request. Try asking something else or saying 'help'."


classifier_model = train_classifier(patterns)
while True:
    user_input = listen()
    bot_response = respond(user_input)
    print("Chatbot:", bot_response)
