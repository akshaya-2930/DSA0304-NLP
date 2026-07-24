import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist

# Download required NLTK resources
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

text = """
Natural Language Processing is a branch of Artificial Intelligence.
It helps computers understand and process human language.
NLP is used in chatbots, machine translation and sentiment analysis.
It is also useful for text summarization and speech recognition.
NLP has become an important technology in modern applications.
"""

# Sentence tokenization
sentences = sent_tokenize(text)

# Word tokenization
words = word_tokenize(text.lower())

# Remove stopwords and punctuation
stop_words = set(stopwords.words('english'))

filtered_words = [
    word for word in words
    if word.isalpha() and word not in stop_words
]

# Calculate word frequencies
frequency = FreqDist(filtered_words)

# Calculate score for each sentence
sentence_scores = {}

for sentence in sentences:
    score = 0

    for word in word_tokenize(sentence.lower()):
        if word in frequency:
            score += frequency[word]

    sentence_scores[sentence] = score

# Select the two highest-scoring sentences
summary_sentences = sorted(
    sentence_scores,
    key=sentence_scores.get,
    reverse=True
)[:2]

print("Original Text:")
print(text)

print("Summary:")
for sentence in summary_sentences:
    print(sentence)