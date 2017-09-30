import csv
Hello_answer = ['Привет!', 'Здравствуйте!', 'Добрый день :)']
How_are_you_answer = ['Все прекрасно!', 'жизнь тлен', 'хочется чая и немножечко сдохнуть']
Goodbye_answer = ['покасики','досвидос', 'увидимся :3']

dict = [{'key':'hello','value':'приветос'}]


with open('export.csv','w', encoding='utf-8') as f:
    fields = ['key','value']
    writer = csv.DictWriter(f,fields,delimiter = ';')
    writer.writeheader()
    for item in dict:
        writer.writerow(item)