from adapters.repository import AbstractRepository
from domain.model import Building, BuildingSection


def createBuilding(building: Building, repo: AbstractRepository, session):
    repo.add(building)
    session.commit()


def createBuildingSection(building_section: BuildingSection, repo: AbstractRepository, session):
    building = repo.get(building_section.building_id)
    building.building_sections.add(building_section)
    session.commit()
