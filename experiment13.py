import nltk
from nltk.classify import NaiveBayesClassifier

# Training Data
training_data = [
    ({'word': 'good'}, 'Positive'),
    ({'word': 'excellent'}, 'Positive'),
    ({'word': 'happy'}, 'Positive'),
    ({'word': 'bad'}, 'Negative'),
    ({'word': 'poor'}, 'Negative'),
    ({'word': 'sad'}, 'Negative')
]

# Train the classifier
classifier = NaiveBayesClassifier.train(training_data)

# Test Data
test_word = {'word': 'excellent'}

# Prediction
result = classifier.classify(test_word)

print("Test Word:", test_word['word'])
print("Predicted Class:", result)