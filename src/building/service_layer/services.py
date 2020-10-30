from building.adapters.repository import AbstractRepository
from building.domain.model import Building, BuildingSection


def create_building(building: Building, repo: AbstractRepository, session):
    repo.add(building)
    session.commit()


def create_building_section(building_section: BuildingSection, repo: AbstractRepository, session):
    building = repo.get(building_section.building_id)
    building.building_sections.add(building_section)
    session.commit()
