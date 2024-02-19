from patterns import pattern
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import MultiLabelBinarizer
import random

patterns = pattern()

user_input = [" ".join(entry["pattern"]) for entry in patterns]
bot_output = [entry["responses"] for entry in patterns]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(user_input)

mlb = MultiLabelBinarizer()
y = mlb.fit_transform(bot_output)

classifier = RandomForestClassifier()
classifier.fit(X, y)


while True:
    usrInput = input("User: ")
    input_vectorized = vectorizer.transform([usrInput])
    predicted_responses_binary = classifier.predict(input_vectorized)
    predicted_responses = mlb.inverse_transform(predicted_responses_binary)
    #print(predicted_responses)
    if predicted_responses and predicted_responses[0]:
        bot_response = random.choice(predicted_responses[0])
    else:
        bot_response = "I couldn't get that"
    print("Chatbot:", bot_response)