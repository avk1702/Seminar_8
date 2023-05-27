
def read_csv(filename: str) -> list:
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    return data

def show_record(record: dict):
    for key in record:
        print(f'{key} : {record[key]}')

def show_menu() -> int:
    print("\n Выберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Сохранить справочник в текстовом формате\n"
          "6. Изменить данные абонента\n"
          "7. Удалить абонента \n"
          "8. Закончить работу")
    choice = int(input())
    return choice 
 
def show_phonebook(phone_book: list):
    for i in phone_book:
        show_record(i)
        print()

def get_search_surname():
    return input("Введите фамилию для поиска: ")
       
def find_by_surname(phone_book: list, surname: str):
    res = []
    for i in phone_book:
        if i["Фамилия"] == surname:                     
           res.append(i)
        
    return res

def get_search_number():
    return input("Введите номер телефона для поиска: ")

def find_by_number(phone_book: list, number: str):
    res = []
    for i in phone_book:
        if i["Телефон"] == number:                     
           res.append(i)
        
    return res

def get_new_user():
    record = dict()
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    for i in fields:
       record[i] = input(f"Введите {i} ")
    return record

def add_user(phone_book, record:dict):
    phone_book.append(record)

def write_csv(filename: str, data: list):
    with open(filename, 'w', encoding='utf-8') as fout:
        for i in range(len(data)):
            s = ''
            for v in data[i].values():
                s += v + ','
            fout.write(f'{s[:-1]}\n')   

def write_txt(filename: str, data: list):
    with open(filename, 'w', encoding='utf-8') as fout:
        for i in range(len(data)):
            s = ''
            for v in data[i].values():
                s += v + ','
            fout.write(f'{s[:-1]}\n')

def change_data(phone_book):
    sub = input("Введите фамилию пользователя: ")
    change = input("Введите, что Вы хотите изменть: ")
    change_data = input("Введите новое значение: ")
    for i in phone_book:
        for v in i.values():
            if v == sub:
                i[change] = i[change].replace(i[change],change_data )

def delete_user(phone_book):
    sub = input("Введите фамилию пользователя: ")
    for i in phone_book:
        for v in i.values():
            if v == sub:
                phone_book.remove(i)
            
def work_with_phonebook():
    choice = show_menu()
    phone_book = read_csv('phonebook.csv')

    while (0 < choice < 9):
        if choice == 1:
            show_phonebook(phone_book)
        elif choice == 2:
            surname = get_search_surname()
            show_phonebook(find_by_surname(phone_book, surname))
        elif choice == 3:
            number = get_search_number()
            show_phonebook(find_by_number(phone_book, number))
        elif choice == 4:
            user_data = get_new_user()
            add_user(phone_book, user_data)
            write_csv('phonebook.csv', phone_book)
        elif choice == 5:
            write_txt('phon.txt', phone_book)
        elif choice == 6:
           change_data(phone_book)
           write_csv('phonebook.csv', phone_book)
        elif choice == 7:
           delete_user(phone_book)
           write_csv('phonebook.csv', phone_book)     
        elif choice == 8:break

        choice = show_menu()
  
if __name__ == '__main__':           
    work_with_phonebook()             