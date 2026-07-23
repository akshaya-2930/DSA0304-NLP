import nltk
from nltk.wsd import lesk
from nltk.tokenize import word_tokenize

# Download required resources
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('wordnet')

sentence = "I went to the bank to deposit money."

words = word_tokenize(sentence)

sense = lesk(words, 'bank')

print("Sentence:")
print(sentence)

print("\nWord:", "bank")

print("\nPredicted Meaning:")
print(sense)

print("\nDefinition:")
print(sense.definition())