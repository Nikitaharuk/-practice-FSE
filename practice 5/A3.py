def abbreviation(text):
    words = text.split()
    abbreviation = ""
    for word in words:
        if len(word) >= 3:
            abbreviation += word[0].upper()
    return abbreviation
text = input("Введите текст: ")
result = abbreviation(text)
print(result)