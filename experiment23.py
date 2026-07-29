from nltk.tokenize import sent_tokenize
import nltk

nltk.download('punkt')
nltk.download('punkt_tab')

text = """
Natural Language Processing is a branch of AI.
It is used in chatbots.
It helps computers understand human language.
"""

sentences = sent_tokenize(text)

print("Number of Sentences:", len(sentences))

if len(sentences) > 1:
    print("The text is coherent.")
else:
    print("The text is not coherent.")