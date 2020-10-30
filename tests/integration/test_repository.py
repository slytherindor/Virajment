import pytest
from building.adapters import repository
from building.domain import model

from tests.random_refs import random_building_id

pytestmark = pytest.mark.usefixtures('mappers')


def test_get_by_building_id(sqlite_session_factory):
    session = sqlite_session_factory()
    repo = repository.SqlAlchemyBuildingRepository(session)
    b1_id = random_building_id()
    b1 = model.Building(
    name="Shopify",
    address="110 Elgin Street",
    zipcode="K1C 3DS",
    city="Ottawa",
    province="ON",
    building_id=b1_id)

    b2_id = random_building_id()
    b2 = model.Building(
        name="IBM",
        address="110 Clarence Street",
        zipcode="K4E 5KS",
        city="Ottawa",
        province="ON",
        building_id=b2_id)

    repo.add(b1)
    repo.add(b2)
    assert repo.get(b1_id) == b1
    assert repo.get(b2_id) == b2


def test_get_all_building_sections_in_building(sqlite_session_factory):
    session = sqlite_session_factory()
    repo = repository.SqlAlchemyBuildingRepository(session)
    b1_id = random_building_id()
    b1 = model.Building(
        name="Shopify",
        address="110 Elgin Street",
        zipcode="K1C 3DS",
        city="Ottawa",
        province="ON",
        building_id=b1_id)

    building_section = model.BuildingSection(building_id=b1_id, floor='23', room='12')
    b1.building_sections.add(building_section)
    repo.add(b1)
    building_received = repo.get(b1_id)
    assert len(building_received.building_sections) == 1
