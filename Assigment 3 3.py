import re

text = """
Meeting on 12/09/2026
Call 9876543210
#NLP
@OpenAI
natural language processing
"""

print("Text:")
print(text)

print("1. Search Date")
print("2. Search Phone Number")
print("3. Search Hashtag")
print("4. Search Mention")
print("5. Search Prefix")
print("6. Search Suffix")

# Direct selection
choice = 1

if choice == 1:
    matches = re.findall(r'\b\d{2}/\d{2}/\d{4}\b', text)
    print("Dates Found:", matches)

elif choice == 2:
    matches = re.findall(r'\b[6-9]\d{9}\b', text)
    print("Phone Numbers Found:", matches)

elif choice == 3:
    matches = re.findall(r'#\w+', text)
    print("Hashtags Found:", matches)

elif choice == 4:
    matches = re.findall(r'@\w+', text)
    print("Mentions Found:", matches)

elif choice == 5:
    prefix = "nat"
    matches = re.findall(r'\b' + re.escape(prefix) + r'\w*', text, re.IGNORECASE)
    print("Words with Prefix", prefix + ":", matches)

elif choice == 6:
    suffix = "ing"
    matches = re.findall(r'\b\w*' + re.escape(suffix) + r'\b', text, re.IGNORECASE)
    print("Words with Suffix", suffix + ":", matches)

else:
    print("Invalid Choice")