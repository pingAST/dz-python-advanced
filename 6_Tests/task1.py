from typing import List

'''
Задание «Сезон года»
'''
# Задача №1


def check_month(month: int):
    if month < 1 or month > 12:
        return "Некорректный номер месяца"
    elif month in [1, 2, 12]:
        return "Зима"
    elif month in [3, 4, 5]:
        return "Весна"
    elif month in [6, 7, 8]:
        return "Лето"
    else:
        return "Осень"


'''

Задание «ФИО»
'''


def fio(initials: List[str]) -> str:
    result = ""
    for name in initials:
        first_letter = name[0]  # получаем первую букву имени, фамилии или отчества
        result += first_letter  # добавляем ее к результату
    return result


'''
Задание «Секретарь»
'''
# Задача №3


documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "driver license", "number": "5455 028765", "name": "Василий Иванов"},
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def get_name(doc_number):
    """
    Функция для поиска имени человека по номеру документа.
    """
    for document in documents:
        if document['number'] == doc_number:
            return document['name']
    return "Документ не найден"


def get_directory(doc_number):
    """
    Функция для поиска номера полки по номеру документа.
    """
    for directory, docs in directories.items():
        if doc_number in docs:
            return directory
    return "Полки с таким документом не найдено"


def add(document_type, number, name, shelf_number):
    """
    Функция для добавления нового документа в каталог и перечень полок.
    """
    documents.append({"type": document_type, "number": number, "name": name})
    if shelf_number in directories:
        directories[shelf_number].append(number)
    else:
        directories[shelf_number] = [number]


if __name__ == '__main__':
    # Задача №1
    season = check_month(1)
    assert season == 'Зима', "Ответ должен быть Зима"
    print(f"1 месяц время года: {season}")
    season = check_month(4)
    assert season == 'Весна', "Ответ должен быть Весна"
    print(f"4 месяц время года: {season}")
    season = check_month(18)
    assert season == "Некорректный номер месяца", "Ответ должен быть 'Некорректный номер месяца'"
    print(f"18 месяц: {season}")

    # Задача №2
    assert fio(['Иванов', 'Иван', 'Иванович']) == 'ИИИ'
    assert fio(['Жан', 'Клот', 'Вандамович']) == 'ЖКВ'
    assert fio(['Павлов', 'Иван', 'Уралович']) == 'ПИУ'
    assert fio(['Семейный', 'Доминик', 'Торретович']) == 'СДТ'
    print("\nОтличная работа, отправляйте на проверку!")

    # Задача №3
    print(get_name("10006"))
    print(get_directory("11-2"))
    print(get_name("101"))
    add('international passport', '311 020203', 'Александр Пушкин', 3)
    print(get_directory("311 020203"))
    print(get_name("311 020203"))
    print(get_directory("311 020204"))
