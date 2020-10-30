import pytest
from . import api_client


@pytest.mark.usefixtures('postgres_db')
@pytest.mark.usefixtures('restart_api')
def test_happy_path_returns_201_and_building_created():
    r = api_client.post_to_add_building("Shopify", "120 Elgin St", "K2D F4D", "Ottawa", "ON")
    assert r.status_code == 201


@pytest.mark.usefixtures('postgres_db')
@pytest.mark.usefixtures('restart_api')
def test_bad_path_returns_201_and_building_created():
    r = api_client.post_to_add_building("120 Elgin St", "K2D F4D", "Ottawa", "ON", 1)
    assert r.status_code == 400
