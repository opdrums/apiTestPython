import requests
import pytest
import json
import os
from dotenv import load_dotenv


base_url = "https://jsonplaceholder.typicode.com/"
load_dotenv()

@pytest.fixture
def get_base_url():
    return base_url

def json_data():
    file_path = os.path.join(os.getenv("RUTA", "."), "data.json")
    if not os.path.exists(file_path):
        pytest.fail(f"El archivo {file_path} no existe en el directorio actual.")

    with open(file_path, "r") as file:
        return json.load(file)

def test_get_user_200(get_base_url):
    response = requests.get(f"{get_base_url}/posts")
    assert response.status_code == 200

def test_validate_longitud_date(get_base_url):
    response = requests.get(f"{get_base_url}/posts")
    data = response.json()
    assert len(data) > 0
    assert json_data()[0]["userId"] == 1

def test_validate_field_date(get_base_url):
    response = requests.get(f"{get_base_url}/posts")
    data = response.json()
    assert data[0]["userId"] <= 1

def test_validate_string_date(get_base_url):
    response = requests.get(f"{get_base_url}/posts")
    data = response.json()
    assert isinstance(data[0]["title"], str)

def test_validate_int_date(get_base_url):
    response = requests.get(f"{get_base_url}/posts")
    data = response.json()
    assert len(data) > 0
    assert isinstance(data, list)
    assert  isinstance(data[0]["userId"], int)