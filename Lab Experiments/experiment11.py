import nltk
from nltk.util import ngrams
from nltk.tokenize import word_tokenize

# Download resources (Run only once)
nltk.download('punkt')
nltk.download('punkt_tab')

text = "Natural Language Processing is very interesting"

words = word_tokenize(text)

print("Words:")
print(words)

# Unigrams
print("\nUnigrams:")
for unigram in ngrams(words, 1):
    print(unigram)

# Bigrams
print("\nBigrams:")
for bigram in ngrams(words, 2):
    print(bigram)

# Trigrams
print("\nTrigrams:")
for trigram in ngrams(words, 3):
    print(trigram)