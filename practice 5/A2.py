import re

def split(text):
    sentences = re.findall(r'[^.!?]*[.!?]', text.strip())
    return sentences
text = input("Введите текст: ")
sentences = split(text)
print("\nВывод:")
for sentence in sentences:
    print(sentence)
print(f"предложений в тексте: {len(sentences)}