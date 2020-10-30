from building.domain.model import Building
from flask import Flask, jsonify, request, make_response
from building.service_layer import services
import uuid
from building.adapters.repository import SqlAlchemyBuildingRepository
from building.adapters.orm import metadata, start_mappers
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from building import config

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
