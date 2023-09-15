# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию,
# и Вы должны реализовать функционал для изменения и удаления данных
from pathlib import Path
list_cont = Path('data.txt')

def record_cont():
    name = input('Введите имя:')
    surmame = input('Введите фамилию:')
    tel = input('Введите телефон:')
    with open('data.txt', 'a') as file_data:
        file_data.write(f'\n{name}, {surmame}, {tel}')

def find_cont():
    fin = input('Введите имя или фамилию для поиска:')
    with open('data.txt','r') as f:
        lines = f.readlines()
        for line in lines:
            if fin in line:
                print(line)

def delete():
    with open(list_cont,'r') as f:
        book = f.read()
        print(book)
        del_tel = int(input('Введите номер контакта для удаления:'))
        tel_book = book.split('\n')
        del_tel_line = tel_book[del_tel]
        tel_book.pop(del_tel)
        print(f'удаленный контакт ->{del_tel_line}\n')
        with open(list_cont,'w') as f:
            f.write('\n'.join(tel_book))

def replace():
    with open(list_cont,'r') as f:
        tel_book = f.read()
    print(tel_book)
    rep_tel = int(input('Введите номер строки для редактирования'))
    tel_book_lines = tel_book.split('\n')
    rep_tel_book_lines = tel_book_lines[rep_tel]
    elements = rep_tel_book_lines.split(',')
    name = input('Введите имя:')
    surmame = input('Введите фамилию:')
    tel = input('Введите телефон:')
    if len(name) == 0:
        name = elements[0]
    if len(surmame) == 0:
        surmame = elements[1]
    if len(tel) == 0:
        tel = elements[2]
    mod_line = (f'{name}, {surmame}, {tel}')
    tel_book_lines[rep_tel] = mod_line
    print(f'Контакт — {rep_tel_book_lines}, изменен на — {mod_line}\n')
    with open(list_cont,'w') as f:
        f.write('\n'.join(tel_book_lines))

def menu_tel():
    choice = int(input('Введите пункт: "1 - Запись контакта" "2 - Поиска контакта" '
                       '"3 - Удаление контакта" "4 - Изменить контакт"->'))
    if choice == 1:
        return record_cont()
    if choice == 2:
        return find_cont()
    if choice == 3:
        return delete()
    if choice == 4:
        return replace()
menu_tel()