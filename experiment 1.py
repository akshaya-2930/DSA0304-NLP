import re

# Sample text
text = "My name is Akshaya. My phone number is 9876543210 and my email is akshaya@gmail.com."

print("Original Text:")
print(text)

# Search for phone number
phone_pattern = r"\b\d{10}\b"
phone = re.search(phone_pattern, text)

if phone:
    print("\nPhone Number Found:", phone.group())
else:
    print("\nPhone Number Not Found")

# Search for email address
email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
email = re.search(email_pattern, text)

if email:
    print("Email Found:", email.group())
else:
    print("Email Not Found")

# Find all words starting with 'M'
pattern = r"\bM\w*"
words = re.findall(pattern, text)

print("Words starting with 'M':", words)

# Replace Geethika with Student
new_text = re.sub(r"Akshaya", "Student", text)

print("\nModified Text:")
print(new_text)