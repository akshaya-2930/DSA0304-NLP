import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

nltk.download('punkt')
nltk.download('punkt_tab')

text = "apple banana apple orange banana apple"

words = word_tokenize(text)

fd = FreqDist(words)

print("Word Frequency:")

for word in fd:
    print(word, ":", fd[word])