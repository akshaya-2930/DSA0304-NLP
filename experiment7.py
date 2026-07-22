import nltk
from nltk import word_tokenize, pos_tag, ne_chunk

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('maxent_ne_chunker_tab')
nltk.download('words')

text = "Ravi works at Microsoft in Hyderabad."

words = word_tokenize(text)
tags = pos_tag(words)

tree = ne_chunk(tags)

print(tree)