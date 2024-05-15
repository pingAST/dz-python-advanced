import pytest
from task1 import check_month, fio, get_name, get_directory, add


@pytest.mark.parametrize("month, expected_season", [
    (1, "Зима"),
    (4, "Весна"),
    (7, "Лето"),
    (13, "Некорректный номер месяца")
])
def test_check_month(month, expected_season):
    season = check_month(month)
    assert season == expected_season


@pytest.mark.parametrize("initials, expected_output", [
    (['Иванов', 'Иван', 'Иванович'], 'ИИИ'),
    (['Жан', 'Клот', 'Вандамович'], 'ЖКВ'),
    (['Павлов', 'Иван', 'Уралович'], 'ПИУ'),
    (['Семейный', 'Доминик', 'Торретович'], 'СДТ')
])
def test_fio(initials, expected_output):
    assert fio(initials) == expected_output


@pytest.mark.parametrize("doc_number, expected_name", [
    ("10006", "Аристарх Павлов"),
    ("11-2", "Геннадий Покемонов"),
    ("101", "Документ не найден")
])
def test_get_name(doc_number, expected_name):
    assert get_name(doc_number) == expected_name


@pytest.mark.parametrize("doc_number, expected_directory", [
    ("10006", '2'),
    ("11-2", '1'),
    ("101", 'Полки с таким документом не найдено')
])
def test_get_directory(doc_number, expected_directory):
    assert get_directory(doc_number) == expected_directory


@pytest.mark.parametrize("doc_type, number, name, shelf_number, expected_directory", [
    ('international passport', '311 020203', 'Александр Пушкин', '3', '3')
])
def test_add(doc_type, number, name, shelf_number, expected_directory):
    add(doc_type, number, name, shelf_number)
    assert get_directory(number) == expected_directory
