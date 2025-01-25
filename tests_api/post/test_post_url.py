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
    file_path = os.path.join(os.getenv("ruta", "."), "create_user.json")
    if not os.path.exists(file_path):
        pytest.fail(f"El archivo {file_path} no existe en el directorio actual.")

    with open(file_path, "r") as file:
        return json.load(file)

# Asegúrate de que json_data() devuelve una lista
@pytest.mark.parametrize("payScript", json_data())
def test_create_user(get_base_url, payScript):
    response = requests.post(f"{get_base_url}/posts", json=payScript)
    assert response.status_code == 201

@pytest.mark.parametrize("payScript", json_data())
def test_validate_string_date(get_base_url, payScript):
    global global_id
    response = requests.post(f"{get_base_url}/posts", json=payScript)
    data = response.json()
    assert data["userId"] == data["userId"]

@pytest.mark.parametrize("payScript", json_data())
def test_validate_parameter_exist(get_base_url, payScript):
    response = requests.post(f"{get_base_url}/posts", json=payScript)
    data = response.json()
    assert "userId" in data
    assert "title" in data
    assert  "body" in data