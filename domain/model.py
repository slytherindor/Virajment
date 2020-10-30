from dataclasses import dataclass


class Building:

    def __init__(self, building_id: str, name: str, address: str, city: str, zipcode: str, province: str):
        self.building_id = building_id
        self.name = name
        self.address = address
        self.city = city
        self.zipcode = zipcode
        self.province = province
        self.building_sections = set()  # type: set[BuildingSection]


class BuildingSection:
    def __init__(self, building_id: int, floor: str, room: str):
        self.building_id = building_id
        self.floor = floor
        self.room = room
        self.__acmdata = None
        self.__leaddata = None
        self.__pcbdata = None

    def __repr__(self):
        return f'<BuildingSectionData {self.floor} {self.room}>'

    def __hash__(self):
        return hash(f'F{self.floor}R{self.room}')


@dataclass(unsafe_hash=True)
class AcmData:
    building_section_id: str
    location: str
    component: str
    material: str
    material_description: str
    sample_number: str
    asbestos: str
    condition: str
    qty: str
    unit: str
    access: str
    control: str
    notes: str


@dataclass(unsafe_hash=True)
class LeadData:
    building_section_id: str
    location: str
    sample_id: str
    paint_colour: str
    lead_concentration: str
    calibration: str
    standard_reading: str
    lead_present: str
    analysis: str
    notes: str


@dataclass(unsafe_hash=True)
class PcbData:
    building_section_id: str
    location: str
    sample_id: str
    item: str
    manufacturer: str
    serial: str
    qty: str
    markings: str
    pcbs: str
    notes: str
