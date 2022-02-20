

with open('referat.txt', 'r', encoding = 'utf-8') as file:
    content = file.read()
    print(content)
    print(len(content))
    
    word_count = content.split(' ')
    print(len(word_count))
    

with open('referat2.txt', 'w', encoding='utf-8') as file:    
    file.write(content.replace('.', '!'))