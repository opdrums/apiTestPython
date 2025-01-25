import requests
import pytest

base_url = "https://jsonplaceholder.typicode.com/"

@pytest.fixture
def get_base_url():
    return base_url

def test_delete_user(get_base_url):
    response = requests.delete(f"{get_base_url}/posts/1")
    assert response.status_code in [200]