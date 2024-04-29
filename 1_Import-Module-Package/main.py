import datetime
import emoji  # пакет emoji, который предоставляет возможность использовать эмодзи в Python
from application.salary import calculate_salary
from application.db.people import get_employees


if __name__ == '__main__':
    print(emoji.emojize(":calendar:Текущая дата:"), datetime.date.today())
    calculate_salary()
    get_employees()