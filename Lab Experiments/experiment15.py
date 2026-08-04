from deep_translator import GoogleTranslator

text = "Good Morning"

translated = GoogleTranslator(source='en', target='te').translate(text)

print("Original Text:")
print(text)

print("\nTranslated Text:")
print(translated)