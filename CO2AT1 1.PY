from tabulate import tabulate

words = ["connected", "connecting", "connection"]

results = []

for word in words:

    if word.endswith("ed"):
        root = "connect"
        suffix = "ed"
        kind = "Inflectional"

    elif word.endswith("ing"):
        root = "connect"
        suffix = "ing"
        kind = "Inflectional"

    elif word.endswith("ion"):
        root = "connect"
        suffix = "ion"
        kind = "Derivational"

    else:
        root = word
        suffix = "-"
        kind = "-"

    results.append([word, root, suffix, kind, root])

print(tabulate(results,
headers=["Word","Root","Suffix","Type","Normalized"],
tablefmt="grid"))