from sqlalchemy import (
    Table, MetaData, Column, Integer, String, Date, ForeignKey, event,
)
from sqlalchemy.orm import mapper, relationship
from domain import model

metadata = MetaData()

building = Table(
    'building', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(255)),
    Column('address', String(255)),
    Column('city', String(255)),
    Column('zipcode', String(255)),
    Column('province', String(255)),
)

acm_data = Table(
    'acm_data', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('location_id', ForeignKey('building_section.id')),
    Column('component', String(255)),
    Column('material', String(255)),
    Column('material_description', String(255)),
    Column('sample_number', String(255)),
    Column('asbestos', String(255)),
    Column('condition', String(255)),
    Column('qty', String(255)),
    Column('unit', String(255)),
    Column('access', String(255)),
    Column('control', String(255)),
    Column('notes', String(255)),
)

lead_data = Table(
    'lead_data', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('location_id', ForeignKey('building_section.id')),
    Column('sample_id', String(255)),
    Column('paint_colour', String(255)),
    Column('lead_concentration', String(255)),
    Column('calibration', String(255)),
    Column('standard_reading', String(255)),
    Column('lead_present', String(255)),
    Column('analysis', String(255)),
    Column('notes', String(255)),
)

pcb_data = Table(
    'pcb_data', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('location_id', ForeignKey('building_section.id')),
    Column('sample_id', String(255)),
    Column('item', String(255)),
    Column('manufacturer', String(255)),
    Column('serial', String(255)),
    Column('qty', String(255)),
    Column('markings', String(255)),
    Column('pcbs', String(255)),
    Column('notes', String(255)),
)

building_section = Table(
    'building_section', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('building_id', ForeignKey('building.id')),
    Column('floor', String(255)),
    Column('room', String(255)),
    Column('location', String(255)),
)

def start_mappers():
    building_section_mapper = mapper(model.BuildingSection, building_section)
    mapper(model.Building, building, properties={
        'building_section': relationship(building_section_mapper)
    })

    acm_data_mapper = mapper(model.AcmData, acm_data)
    lead_data_mapper = mapper(model.LeadData, lead_data)
    pcb_data_mapper = mapper(model.PcbData, pcb_data)

