from tabulate import tabulate

words = ["played", "player", "playing"]

results = []

for word in words:

    if word.endswith("ed"):
        stem = "play"
        affix = "ed"
        kind = "Inflectional"

    elif word.endswith("ing"):
        stem = "play"
        affix = "ing"
        kind = "Inflectional"

    elif word.endswith("er"):
        stem = "play"
        affix = "er"
        kind = "Derivational"

    else:
        stem = word
        affix = "-"
        kind = "-"

    results.append([word,stem,affix,kind,stem])

print(tabulate(results,
headers=["Word","Stem","Removed Affix","Type","Normalized"],
tablefmt="grid"))