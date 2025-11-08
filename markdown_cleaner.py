import re

def clean_text(text):
    words = re.findall(r'\b[a-zA-Z]+\b', text)
    return ' '.join(words)

# Example input
input_text = "some texts with 123 numbers and #special $characters!"
cleaned_text = clean_text(input_text)
print(cleaned_text)