import requests

access_token = '<token>'
hostname = 'https://cloud-api.yandex.net'


def create_folder(folder_name):
    headers = {
        'Authorization': f'OAuth {access_token}'
    }
    params = {
        'path': folder_name
    }
    response = requests.put(f'{hostname}/v1/disk/resources', params=params, headers=headers)

    if response.status_code == 409:
        print("Папка уже существует. Пожалуйста, введите другое имя папки.")
    elif response.status_code != 201:
        raise Exception(f"Ошибка при создании папки: {response.json()}")

    return response
