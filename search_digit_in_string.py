
d = {0:'{ноль}',
     1:'{один}',
     2:'{два}',
     3:'{три}',
     4:'{четыре}',
     5:'{пять}',
     6:'{шесть}',
     7:'{семь}',
     8:'{восемь}',
     9:'{девять}'
    }

def replace_text_from_template(d:dict):
    """ Заменяет текст по шаблону из словаря:
        ключ словаря - заменяемое слово,
        значение ключа - заменяющее (на которое меняем)
    """
    f = "random_text.txt"
    with open(f, "r", newline='') as f:
        r = f.read()
        print(r[:350],'\n###') # вывод на экран кол-во символов неотредактированного текста
        for i in d:
            r = r.replace(str(i), str(d[i]))

    with open('replace_text.txt', 'w', newline='') as f: # запись в файл
            f.write(r)
            
    print('- СПАСИБО ЗА ОЖИДАНИЕ. ВСЁ ГОТОВО -')
    input('Чтобы открыть файл и прочитать текст нажмите <Enter>')

    f = "replace_text.txt"
    with open(f, "r", newline='') as f:
        print('###')
        print(f.read())

if __name__=='__main__':
    replace_text_from_template(d)
