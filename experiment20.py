from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Training data
texts = [
    "I love this movie",
    "This is amazing",
    "I am very happy",
    "I hate this movie",
    "This is terrible",
    "I am very sad"
]

labels = [
    "Positive",
    "Positive",
    "Positive",
    "Negative",
    "Negative",
    "Negative"
]

# Convert text into numerical features
vectorizer = CountVectorizer()

X = vectorizer.fit_transform(texts)

# Train Naive Bayes classifier
model = MultinomialNB()
model.fit(X, labels)

# Test sentence
test_text = ["I love this amazing movie"]

test_vector = vectorizer.transform(test_text)

prediction = model.predict(test_vector)

print("Input Text:")
print(test_text[0])

print("\nPredicted Sentiment:")
print(prediction[0])