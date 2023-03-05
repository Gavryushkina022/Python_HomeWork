#  Фамилия, имя, отчество, номер телефона
from pyautogui import typewrite
import time

def ask_user():
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    phone_number = int(input('Введите номер телефона: '))
    return last_name, first_name, phone_number


def save_to_file(data: tuple, file, mode='a'):
    data_str = ' '.join(map(str, data))
    # print(data_str)
    # 'cp-1251'
    with open(file, mode, encoding='utf-8') as fd:
        fd.write(f'{data_str}\n')


def read_file(file):
    with open(file, 'r', encoding='utf-8') as fd:
        lines = fd.readlines()
    headers = ['фамилия', 'имя', 'номер телефона']
    list_contacts = []
    for line in lines:
        line = line.strip().split()
        list_contacts.append(dict(zip(headers, line)))
    return list_contacts


def search_contact(list_contacts: list, param: str, what: str):
    param_dict = {'1': 'фамилия', '2': 'имя', '3': 'номер телефона'}
    found_contacts = []
    for contact in list_contacts:
        if contact[param_dict[param]] == what:
            found_contacts.append(contact)
    return found_contacts


def ask_search():
    print('По какому полю выполнить поиск?')
    search_param = input('1 - по фамилии, 2 - по имени, 3 - по номеру телефона: ')
    what = None
    if search_param == '1':
        what = input('Введите фамилию для поиска: ')
    elif search_param == '2':
        what = input('Введите имя для поиска: ')
    elif search_param == '3':
        what = input('Введите номер для поиска: ')
    return search_param, what

# Update record
def update_record(name_file):
    lst_contacts = read_file(name_file)
    search = input("Введите имя или фамилию для изменения: ")
    count_of_search = 0
    for contact in lst_contacts:
        if contact['фамилия'] == search or contact['имя'] == search:
            count_of_search = +1
            print(contact)
            print("Найден контакт" + str(contact))
            what = input("Выберите - 1-изменить его,2-нет и продолжить поиск, 3-выйти: ")
            if what == '1':
                print("Измените фамилию или нажмите Enter: ")
                # Вводим слип так как принт бывает отрабатывает с запозданием
                time.sleep(0.2)
                typewrite(contact['фамилия'])
                contact['фамилия'] = input()
                print("Измените имя или нажмите Enter: ")
                time.sleep(0.2)
                typewrite(contact['имя'])
                contact['имя'] = input()
                print("Измените номер телефона или нажмите Enter: ")
                time.sleep(0.2)
                typewrite(contact['номер телефона'])
                contact['номер телефона'] = input()
                print("Запись изменена!")
            elif what == '2':
                continue
            else:
                save_all(name_file, lst_contacts)
                break

            what = input("Продолжить поиск контактов с таким же именем и фамилией 1-да 2-нет: ")
            if what == '1':
                continue
            else:
                save_all(name_file, lst_contacts)
                break

        if count_of_search == 0:
            print('Запись с таким именем или фамилией не найдена...')
        else:
            save_all(name_file, lst_contacts)


# Save list
def save_all(name_file, data: list):
    open(name_file, 'w').close()
    for contact in data:
        save_to_file(tuple(contact.values()), name_file)


# Remove record
def remove_record(name_file, ):
    what = input('Введите имя или фамилию для удаления: ')
    lst_contacts_after_delete = []
    lst_contacts = read_file(name_file)
    for contact in lst_contacts:
        if contact['фамилия'] != what and contact['имя'] != what:
            lst_contacts_after_delete.append(contact)

    quantity_remove_record = len(lst_contacts) - len(lst_contacts_after_delete)
    if quantity_remove_record == 0:
        print('Запись с таким именем или фамилией не найдена...')
    else:
        save_all(name_file, lst_contacts_after_delete)
        print('Удалено записей: ' + str(quantity_remove_record))


def main_menu():
    file_contacts = 'file.txt'
    while True:
        user_choice = input('1 - добавить новый контакт,'
                            '\n 2 - найти контакт,'
                            '\n 3 - посмотреть весь справочник,'
                            '\n 4 - обновить запись в справочнике,'
                            '\n 5 - удалить запись в справочнике,'
                            '\n 0 - выйти\n')
        if user_choice == '1':
            # print('добавить новый контакт')
            save_to_file(ask_user(), file_contacts)
        elif user_choice == '2':
            # print('найти контакт')
            lst_contacts = read_file(file_contacts)
            search_param, what = ask_search()
            res = search_contact(lst_contacts, search_param, what)
            print(res)
        elif user_choice == '3':
            # print('посмотреть весь справочник')
            print(read_file(file_contacts))
        elif user_choice == '4':
            update_record(file_contacts)
            print()
        elif user_choice == '5':
            remove_record(file_contacts)
        elif user_choice == '0':
            print('До свидания')
            break


if __name__ == '__main__':
    main_menu()
    # # data = ask_user()
    # # print(data)
    # # save_to_file(data, file_contacts)
    # lst_contacts = read_file(file_contacts)
    # print(lst_contacts)
    # search_param, what = ask_search()
    # res = search_contact(lst_contacts, search_param, what)
    # print(res)
    # # lst1 = [1, 2, 3]
    # # lst2 = [7, 8, 9]
    # # res = zip(lst1, lst2)
    # # print(dict(res))

# https://docs.python.org/3/library/csv.html
# https://docs-python.ru/standart-library/modul-csv-python/priemy-raboty-modulem-csv/
# https://docs-python.ru/standart-library/modul-sqlite3-python/brief-description/
