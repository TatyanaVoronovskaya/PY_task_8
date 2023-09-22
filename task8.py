# Создать телефонный справочник с возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться
# в файле. 
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа не должна быть линейной

# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных

from pathlib import Path

def Write_Contact(phone_list = 'phBook.txt'):   # функция добавления
    with open('phBook.txt', 'a', encoding="UTF-8") as phone_list:
        first_name = input("Введите фамилию: ")        
        last_name = input("Введите имя: ")
        phone = input("Введите номерок: ")
        phone_list.write(f'\n  {first_name}, {last_name}, {phone}')

def FindContact(phone_list = 'phBook.txt'):  # функция поиска контакта
    with open('phBook.txt', 'r', encoding="UTF-8") as phone_list:
        find_contact = str(input(f'Введите фамилию для поиска? ->'))
        data = phone_list.readlines()
        a = True
        for i in data:
            contact = i.strip().split(',')
            if (find_contact in contact[0]):
                a = False
                print(i)
        if a:
            print("Контакт не найден")

def PrintContacts(phone_list = 'phBook.txt'):  # функция вывода  тел книги
    with open('phBook.txt', 'r', encoding="UTF-8") as phone_list:
        data = phone_list.readlines()
        for i in data:
            print(i, end = '')

def deleteContact(phone_list = 'phBook.txt'):  # Функция удаления контакта из телефонной книги
    with open('phBook.txt', 'r+', encoding="UTF-8") as phone_list:
        data = phone_list.readlines()
        PrintContacts(data)
        fnameContact = str(input(f'\n Кого удаляем? Фамилия: '))
        nameContact = str(input(f'\n Кого удаляем? Имя: '))
        with open('phBook.txt', "w", encoding="UTF-8") as phone_list:
            for i in data:
                contact = i.strip().split(',')
                if not ((fnameContact in contact[0]) and (nameContact in contact[1])):
                    phone_list.write(i)
        print(f"Контакт {fnameContact} {nameContact} удален\n")

def changeContact(phone_list = 'phBook.txt'):  # Функция изменения контакта
    with open('phBook.txt', 'r+', encoding="UTF-8") as phone_list:
        data = phone_list.readlines()
        PrintContacts(data)
        fnameContact = str(input(f'\n Какой контакт нужно изменить? Фамилия: '))
        nameContact = str(input(f'\n Какой контакт нужно изменить? Имя: '))
        with open('phBook.txt', "w", encoding="UTF-8") as phone_list:
            for i in data:
                contact = i.strip().split(',')
                if not ((fnameContact in contact[0]) and (nameContact in contact[1])):
                    phone_list.write(i)
        with open('phBook.txt', "a", encoding="UTF-8") as phone_list:
            last_name = input("Меняем фамилию контакта? -> ")        
            first_name = input("Меняем имя контакта? ->: ")
            phone = input("Введите новый номерок: ")
            phone_list.write(f'\n  {last_name}, {first_name}, {phone}')
        print(f"Контакт изменен\n")     

def main(phone_list = 'phBook.txt'):  # Функция реализации главного меню
    Choice = int(input(" Введите номер меню (от 1 до 5, 0 - выход): "))
    if Choice == 1:
            Write_Contact(phone_list)
    elif Choice == 2:
            FindContact(phone_list)
    elif Choice == 3:
            PrintContacts(phone_list)
    elif Choice == 4:
            deleteContact(phone_list)
    elif Choice == 5:
            changeContact(phone_list)
    elif Choice == 0:
            print("Выход из меню")
            return
    

def menu():                                  # Функция выбора операции
    print("ТЕЛЕФОННЫЙ СПРАВОЧНИК")
    print("1 --- Ввести новый контакт")
    print("2 --- Найти контакт")
    print("3 --- Вывести все контакты в книге")
    print("4 --- Удалить контакт")
    print("5 --- Изменить контакт")
    print("0 --- Выход")
    print("\n")
    
menu()
main()