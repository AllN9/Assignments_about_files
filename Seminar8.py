def show_menu():
    print('1. Распечатать справочник\n'
          '2. Найти телефон по фамилии\n'
          '3. Изменить номер телефона\n'
          '4. Удалить запись\n'
          '5. Найти абонента по номеру телефона\n'
          '6. Добавить абонента в справочник\n'
          '7. Скопировать строку в новый файл\n'
          '8. Вывести меню еще раз\n'
          '9. Закончить работу\n', sep = '\n')

def work_with_phonebook():
    choice = show_menu()
    choice = int(input())

    while(choice != 9):
        phone_book = read_txt('directory.txt')

        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            last_name = input('lastname - ')
            print(find_by_lasname(phone_book, last_name))
        elif choice == 3:
            last_name = input('lastname - ')
            new_number = input('new number - ')
            change_number(phone_book, last_name, new_number)
        elif choice == 4:
            last_name = input('lastname - ')
            delete_by_lastname(phone_book, last_name)
        elif choice == 5:
            number = input('number - ')
            print(find_my_number(phone_book, number))
        elif choice == 6:
            print('Введите фамилию, имя, телефон и краткое описание через запятую без пробелов:')
            user_data = input('new data - ')
            add_user(user_data)
        elif choice == 7:
            new_str = input('number of str - ')
            file = input('name of new file - ')
            make_new_str_in_file(phone_book, new_str, file)
        elif choice == 8:
            choice = show_menu()
        
        choice = int(input())

def read_txt(filename):
    phone_book = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']

    with open(filename, 'r', encoding = 'utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.split(',')))
            phone_book.append(record)
    
    return phone_book

def write_txt(filename, phone_book):

    with open(filename, 'w', encoding = 'utf-8') as phout:
        for i in range(len(phone_book)):
            s = ''
            for v in phone_book[i].values():
                s += v + ','
            phout.write(f'{s[:-1]}')

def  print_result(phone_book):
    for i in range(len(phone_book)):
        print(phone_book[i].get('Фамилия'),',', phone_book[i].get('Имя'),',', phone_book[i].get('Телефон'),',', phone_book[i].get('Описание'))

def find_by_lasname(phone_book, last_name):
    number = ''

    for i in range(len(phone_book) - 1):
        if(phone_book[i].get('Фамилия') == last_name):
            number = number + phone_book[i].get('Телефон') + ','
    return number[:-1]

def change_number(phone_book, last_name, new_number):
    for i in range(len(phone_book)):
        if(phone_book[i].get('Фамилия') == last_name):
            phone_book[i]['Телефон'] = new_number
    
    with open('directory.txt', 'w', encoding = 'utf-8') as phout:
        for i in range(len(phone_book)):
            s = ''
            for v in phone_book[i].values():
                s += v + ','
            phout.write(f'{s[:-1]}')

def delete_by_lastname(phone_book, last_name):
    for i in range(len(phone_book)):
        if(phone_book[i].get('Фамилия') == last_name):
            phone_book.pop(i)
    
    with open('directory.txt', 'w', encoding = 'utf-8') as phout:
        for i in range(len(phone_book)):
            s = ''
            for v in phone_book[i].values():
                s += v + ','
            phout.write(f'{s[:-1]}')

def find_my_number(phone_book, number):
    for i in range(len(phone_book) - 1):
        if(phone_book[i].get('Телефон') == number):
            return phone_book[i].get('Фамилия')

def add_user(user_data):
    with open('directory.txt', 'a', encoding = 'utf-8') as file:
        file.write(f'\n{user_data}')

def make_new_str_in_file(phone_book, new_str, file):
    with open(file, 'a', encoding = 'utf-8') as phout:
        for i in range(len(phone_book)):
            s = ''
            if(i == int(new_str) - 1):
                for v in phone_book[i].values():
                    s += v + ','
                phout.write(f'{s[:-1]}')

work_with_phonebook()