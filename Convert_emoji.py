import demoji

# Remove Emoji from Text
text = "Good morning! 😂"
x1 = demoji.replace(text, "")
print(x1, "\n")

# Replace Emoji with Descriptive Text
text = "Happy birthday! 🎂😂"
x2 = demoji.replace_with_desc(text)
print(x2, "\n")

# Detect Emoji in a String
text = "THIS IS A TEXT! 🎮😭"
x3 = demoji.findall(text)
print(x3, "\n")

