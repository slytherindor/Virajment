import uuid

from building import config
from building.adapters.orm import metadata, start_mappers
from building.adapters.repository import (
    SqlAlchemyBuildingRepository, SqlAlchemyLeadDataRepository, SqlAlchemyAcmDataRepository, SqlAlchemyPcbDataRepository
)
from building.domain.model import Building, BuildingSection, LeadData, AcmData, PcbData
from building.service_layer import services
from flask import Flask, jsonify, request, make_response
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)


def init_engine_with_models():
    engine = create_engine(config.get_postgres_uri())
    metadata.create_all(engine)
    return engine


engine_1 = init_engine_with_models()
start_mappers()
get_session = sessionmaker(bind=engine_1)


@app.route("/building", methods=["POST"])
def add_building():
    session = get_session()
    repo = SqlAlchemyBuildingRepository(session)
    try:
        building_uuid = uuid.uuid4().hex[:6]
        building = Building(
            building_uuid,
            request.json['name'],
            request.json['address'],
            request.json['city'],
            request.json['zipcode'],
            request.json['province'],
        )

        services.create_building(building, repo, session=session)
    except Exception as e:
        return jsonify({'message': str(e)}), 400
    return make_response('Created', 201)


@app.route("/building/section", methods=["POST"])
def add_building_section():
    session = get_session()
    repo = SqlAlchemyBuildingRepository(session)
    try:
        building_section = BuildingSection(
            request.json['building_id'],
            request.json['floor'],
            request.json['room'],
        )

        services.create_building_section(building_section, repo, session=session)
    except Exception as e:
        return jsonify({'message': str(e)}), 400
    return make_response('Created', 201)


@app.route("/lead", methods=["POST"])
def add_lead_data():
    session = get_session()
    repo = SqlAlchemyLeadDataRepository(session)
    try:
        lead_data = LeadData(
            request.json['building_section_id'],
            request.json['location'],
            request.json['sample_id'],
            request.json['paint_colour'],
            request.json['lead_concentration'],
            request.json['calibration'],
            request.json['standard_reading'],
            request.json['lead_present'],
            request.json['analysis'],
            request.json['notes'],

        )
        services.create_lead_data(lead_data, repo, session=session)
    except Exception as e:
        return jsonify({'message': str(e)}), 400
    return make_response('Created', 201)


@app.route("/acm", methods=["POST"])
def add_lead_data():
    session = get_session()
    repo = SqlAlchemyAcmDataRepository(session)
    try:
        acm_data = AcmData(
            request.json['building_section_id'],
            request.json['location'],
            request.json['component'],
            request.json['material'],
            request.json['material_description'],
            request.json['sample_number'],
            request.json['asbestos'],
            request.json['condition'],
            request.json['qty'],
            request.json['unit'],
            request.json['access'],
            request.json['control'],
            request.json['notes'],
        )
        services.create_acm_data(acm_data, repo, session=session)
    except Exception as e:
        return jsonify({'message': str(e)}), 400
    return make_response('Created', 201)


@app.route("/pcb", methods=["POST"])
def add_lead_data():
    session = get_session()
    repo = SqlAlchemyPcbDataRepository(session)
    try:
        pcb_data = PcbData(
            request.json['building_section_id'],
            request.json['location'],
            request.json['sample_id'],
            request.json['item'],
            request.json['manufacturer'],
            request.json['serial'],
            request.json['qty'],
            request.json['markings'],
            request.json['pcbs'],
            request.json['notes'],
        )
        services.create_pcb_data(pcb_data, repo, session=session)
    except Exception as e:
        return jsonify({'message': str(e)}), 400
    return make_response('Created', 201)
