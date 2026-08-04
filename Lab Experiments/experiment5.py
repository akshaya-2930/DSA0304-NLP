import nltk
from nltk.stem import PorterStemmer

# Create Porter Stemmer object
ps = PorterStemmer()

words = [
    "playing",
    "running",
    "studies",
    "connected",
    "happiness",
    "flying"
]

print("Original Word -> Stemmed Word")

for word in words:
    print(word, "->", ps.stem(word))