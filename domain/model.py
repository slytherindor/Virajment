from dataclasses import dataclass


@dataclass(unsafe_hash=True)
class Building:
    building_id: str
    name: str
    address: str
    city: str
    zipcode: str
    province: str


class BuildingSection:
    def __init__(self, floor, room, location):
        self.floor = floor
        self.room = room
        self.location = location
        self.__acmdata = None
        self.__leaddata = None
        self.__pcbdata = None

    def __repr__(self):
        return f'<BuildingSectionData {self.floor} {self.room} {self.location}>'

    def __hash__(self):
        return hash(f'F{self.floor}R{self.room}L{self.location})')


@dataclass(unsafe_hash=True)
class AcmData:
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
    sample_id: str
    item: str
    manufacturer: str
    serial: str
    qty: str
    markings: str
    pcbs: str
    notes: str



