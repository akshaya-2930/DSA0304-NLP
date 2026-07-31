from nltk.stem import PorterStemmer
from tabulate import tabulate

ps = PorterStemmer()

words = ["relational", "relation", "relate"]

results = []

for word in words:

    if word == "relational":
        rule = "Remove 'ational' → ate"
        intermediate = "relate"

    elif word == "relation":
        rule = "Remove 'ion'"
        intermediate = "relat"

    elif word == "relate":
        rule = "Remove trailing 'e'"
        intermediate = "relat"

    stem = ps.stem(word)

    results.append([word,rule,intermediate,stem])

print(tabulate(results,
headers=["Word","Applied Rule","Intermediate Form","Final Stem"],
tablefmt="grid"))