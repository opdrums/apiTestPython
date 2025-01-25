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
    file_path = os.path.join(os.getenv("RUTA", "."), "create_user.json")
    if not os.path.exists(file_path):
        pytest.fail(f"El archivo {file_path} no existe en el directorio actual.")

    with open(file_path, "r") as file:
        return json.load(file)

@pytest.mark.parametrize("payScript", json_data())
def test_patch_api(get_base_url, payScript):
    response = requests.patch(f"{get_base_url}/posts/1", json=payScript)
    data = response.json()
    assert response.status_code == 200
    assert data["userId"] in [1,2,3]
