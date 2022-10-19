from unittest.mock import patch as mock_patch
from fastapi.testclient import TestClient
from server import app

client = TestClient(app)


@mock_patch('function that we dont want to test: func')
def test_add_type():
    # func.return_value='charmelon'
    x = client.get('https://w3schools.com')
    print(x.status_code)
    # add eevee  id 133
    # get pokemon by type
    assert sum(
        0, 1) == 1, "Test failed! Wrong total when adding regular number with zero"
