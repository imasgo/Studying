with open('referat.txt','r',encoding = 'utf-8') as f:
    content = f.read()
    words_in_text = content.split()
    print(len(words_in_text))
