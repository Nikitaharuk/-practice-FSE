def sk(text):
    pos1 = text.find('(')
    while (pos1 != -1):
        pos1 = text.find('(')
        pos2 = text.find(')')
        text=text.replace(text[pos1:pos2 +1], '')
    return text
text=input('введите текст ')
print(sk(text))