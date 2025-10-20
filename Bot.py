# chatbot_simple.py

import random
import json
import nltk
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

nltk.download('punkt')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

# Load intents
with open("intents.json", "r") as f:
    data = json.load(f)

# Prepare dataset
texts = []
labels = []
for intent in data['intents']:
    tag = intent['tag']
    for pattern in intent['patterns']:
        texts.append(pattern)
        labels.append(tag)

# Preprocessing function
def preprocess(text):
    tokens = nltk.word_tokenize(text.lower())
    lem = [lemmatizer.lemmatize(tok) for tok in tokens]
    return " ".join(lem)

texts_proc = [preprocess(t) for t in texts]

# Vectorize
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts_proc)

# Train classifier
clf = LogisticRegression()
clf.fit(X, labels)

# Chat loop
def chatbot_response(user_input):
    ui = preprocess(user_input)
    vec = vectorizer.transform([ui])
    pred = clf.predict(vec)[0]
    # confidence / checking threshold could be added
    # find the intent object
    for intent in data['intents']:
        if intent['tag'] == pred:
            return random.choice(intent['responses'])
    return "I’m sorry, I didn’t understand that."

if __name__ == "__main__":
    print("Start chatting! (type 'exit' to quit)")
    while True:
        inp = input("You: ")
        if inp.lower() in ["exit","quit"]:
            break
        res = chatbot_response(inp)
        print("Bot:", res)
