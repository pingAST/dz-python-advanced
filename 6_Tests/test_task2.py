import pytest
from task2 import create_folder


@pytest.mark.parametrize("folder_name, expected_status", [
    ("test_folder_1", 201),
    ("test_folder_2", 201),
    ("test_folder_1", 409)
])
def test_create_folder(folder_name, expected_status):
    response = create_folder(folder_name)
    assert response.status_code == expected_status
