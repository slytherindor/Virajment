from building.adapters.repository import AbstractBuildingRepository, AbstractDataRepository
from building.domain.model import Building, BuildingSection, LeadData, PcbData, AcmData


def create_building(building: Building, repo: AbstractBuildingRepository, session):
    repo.add(building)
    session.commit()


def create_building_section(building_section: BuildingSection, repo: AbstractBuildingRepository, session):
    building = repo.get(building_section.building_id)
    building.building_sections.add(building_section)
    session.commit()


def create_lead_data(data: LeadData, repo: AbstractDataRepository, session):
    repo.add(data)
    session.commit()


def create_pcb_data(data: PcbData, repo: AbstractDataRepository, session):
    repo.add(data)
    session.commit()


def create_acm_data(data: AcmData, repo: AbstractDataRepository, session):
    repo.add(data)
    session.commit()
