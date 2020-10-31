import json
from json import JSONEncoder

from building.adapters.repository import AbstractBuildingRepository, AbstractDataRepository
from building.domain.model import Building, BuildingSection, LeadData, PcbData, AcmData


class BuildingEncoder(JSONEncoder):
    def default(self, obj):
        # an SQLAlchemy class
        fields = {}
        for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
            data = obj.__getattribute__(field)
            try:
                json.dumps(data)  # this will fail on non-encodable values, like other classes
                fields[field] = data
            except TypeError:
                fields[field] = None
        # a json-encodable dict
        return fields

        # return json.JSONEncoder.default(self, obj)


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


def get_building_sections(building_id: str, repo: AbstractBuildingRepository):
    print(building_id)
    building = repo.get(building_id)
    if not building.building_sections:
        return []

    cleaned_data = remove_non_primitive_types_from_object(building.building_sections)
    return cleaned_data


def get_all_buildings(repo: AbstractBuildingRepository):
    data = repo.list()
    json_data = create_buildings_dict(data)
    return json_data


def remove_non_primitive_types_from_object(data):
    cleaned_data = []
    for d in data:
        clean_data = {}
        for (key, value) in d.__dict__.items():
            if not key.startswith('_'):
                clean_data[key] = value
        cleaned_data.append(clean_data)
    print(cleaned_data)
    return cleaned_data


def create_buildings_dict(data):
    json_data = {}
    cleaned_data = remove_non_primitive_types_from_object(data)
    for obj in cleaned_data:
        json_data[obj['building_id']] = obj
    return json_data
