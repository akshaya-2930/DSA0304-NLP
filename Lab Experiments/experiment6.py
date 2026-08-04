import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

text = "The cat is sitting on the mat."

words = word_tokenize(text)
pos_tags = nltk.pos_tag(words)

print("Part-of-Speech Tags:")
print(pos_tags)