dialog = [
    "Hello",
    "How are you?",
    "I am fine.",
    "Thank you",
    "Bye"
]

for sentence in dialog:
    if sentence.endswith("?"):
        print(sentence, "-> Question")
    elif sentence.lower() in ["hello", "hi"]:
        print(sentence, "-> Greeting")
    elif sentence.lower() == "bye":
        print(sentence, "-> Goodbye")
    elif "thank" in sentence.lower():
        print(sentence, "-> Thanks")
    else:
        print(sentence, "-> Statement")