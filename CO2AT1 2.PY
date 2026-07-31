from tabulate import tabulate

words = ["unhappy", "happiness", "happily"]

results = []

for word in words:

    prefix = "-"
    suffix = "-"
    root = "happy"

    if word.startswith("un"):
        prefix = "un"
        suffix = "-"
        kind = "Derivational"

    elif word.endswith("ness"):
        suffix = "ness"
        kind = "Derivational"

    elif word.endswith("ly"):
        suffix = "ly"
        kind = "Derivational"

    else:
        kind = "Inflectional"

    results.append([word,prefix,root,suffix,kind,root])

print(tabulate(results,
headers=["Word","Prefix","Root","Suffix","Type","Normalized"],
tablefmt="grid"))