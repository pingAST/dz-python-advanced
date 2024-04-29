import csv
import re


def read_contacts(file_name):
    with open(file_name, "r", encoding="utf8") as f:
        return list(csv.reader(f, delimiter=","))


def extract_name(name_str):
    return re.findall(r"([(А-ЯЁ][а-яё]+)", name_str)


def format_phone(phone):
    nums = phone_pattern.match(phone)
    if nums.groups()[5]:
        return phone_pattern.sub(r"+7(\2)\3-\4-\5 доб.\6", phone)
    else:
        return phone_pattern.sub(r"+7(\2)\3-\4-\5", phone)


PHONE_PATTERN = r"^(\+7|8)?\D*(\d{3})\D*(\d{3})\D*(\d{2})\D*(\d{2})\D*(\d{4})?.*"
phone_pattern = re.compile(PHONE_PATTERN)

contacts_list = read_contacts("phonebook_raw.csv")
contacts_info = {}

for contact in contacts_list[1:]:
    lastname, firstname, surname, organization, position, phone, email = contact[:7]
    name = extract_name(lastname + firstname + surname)

    if len(name) < 2:
        continue

    full_name = name[0] + name[1]
    if full_name not in contacts_info:
        contacts_info[full_name] = {"lastname": name[0], "firstname": name[1]}
        if len(name) > 2:
            contacts_info[full_name]["surname"] = name[2]

    if organization:
        contacts_info[full_name]["organization"] = organization

    if position:
        contacts_info[full_name]["position"] = position

    if phone:
        contacts_info[full_name]["phone"] = format_phone(phone)

    if email:
        contacts_info[full_name]["email"] = email

contacts_list_up = [[v.get("lastname"), v.get("firstname"), v.get("surname"),
                     v.get("organization"), v.get("position"), v.get("phone"), v.get("email")]
                    for v in contacts_info.values()]

contacts_list_up.insert(0, contacts_list[0])

with open("phonebook.csv", 'w', encoding="utf-8", newline='') as f:
    csv.writer(f, delimiter=',').writerows(contacts_list_up)
