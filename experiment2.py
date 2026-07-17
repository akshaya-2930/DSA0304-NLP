import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

# Download tokenizer (only first time)
nltk.download('punkt')

text = "Natural Language Processing is an interesting subject. Python makes NLP easy."

# Sentence Tokenization
sentences = sent_tokenize(text)
print("Sentence Tokenization:")
for sentence in sentences:
    print(sentence)

print("\nWord Tokenization:")
words = word_tokenize(text)
print(words)