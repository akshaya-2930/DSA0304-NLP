from textblob import TextBlob

text = "I havv a dreem to becme a softwre enginer."

blob = TextBlob(text)

print("Original Text:")
print(blob)

print("\nCorrected Text:")
print(blob.correct())