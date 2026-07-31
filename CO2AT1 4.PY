from tabulate import tabulate

words = ["writes", "writing", "written"]

results = []

for word in words:

    if word == "writes":
        path = "Start → write → s → End"
        root = "write"
        morph = "write + s"
        kind = "Regular"

    elif word == "writing":
        path = "Start → write → ing → End"
        root = "write"
        morph = "write + ing"
        kind = "Regular"

    elif word == "written":
        path = "Start → write → written → End"
        root = "write"
        morph = "write → written"
        kind = "Irregular"

    results.append([word,path,morph,root,kind,root])

print(tabulate(results,
headers=["Word","State Transition","Morphology","Root","Class","Normalized"],
tablefmt="grid"))