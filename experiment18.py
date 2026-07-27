from sklearn.feature_extraction.text import CountVectorizer

documents = [
    "Natural Language Processing is interesting",
    "Python is useful for Natural Language Processing",
    "Python is easy to learn"
]

vectorizer = CountVectorizer()

bow_matrix = vectorizer.fit_transform(documents)

print("Vocabulary:")
print(vectorizer.get_feature_names_out())

print("\nBag of Words Matrix:")
print(bow_matrix.toarray())