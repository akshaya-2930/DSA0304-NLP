import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Download required resources (Run only once)
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('omw-1.4')

text = "The children are playing with the toys."

# Tokenize the sentence
words = word_tokenize(text)

# Create lemmatizer
lemmatizer = WordNetLemmatizer()

print("Original Words:")
print(words)

print("\nMorphological Analysis (Lemmatization):")
for word in words:
    print(word, "->", lemmatizer.lemmatize(word))