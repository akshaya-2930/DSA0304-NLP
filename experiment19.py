from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

document1 = "Natural Language Processing is interesting"
document2 = "Natural Language Processing is useful"

documents = [document1, document2]

vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform(documents)

similarity = cosine_similarity(
    tfidf_matrix[0:1],
    tfidf_matrix[1:2]
)

print("Document 1:")
print(document1)

print("\nDocument 2:")
print(document2)

print("\nCosine Similarity:")
print(round(similarity[0][0], 4))