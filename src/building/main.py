from sqlalchemy import create_engine
from src.building.adapters import orm
from sqlalchemy.orm import sessionmaker
from src.building import config
from src.building.domain.model import Building, BuildingSection
from src.building.adapters.repository import SqlAlchemyBuildingRepository


def init_engine_with_models():
    engine = create_engine(config.get_postgres_uri())
    orm.metadata.create_all(engine)
    return engine


# engine = init_engine_with_models()
orm.start_mappers()
get_session = sessionmaker(bind=init_engine_with_models())


building1 = Building(
    name="Shopify",
    address="110 Elgin Street",
    zipcode="K1C 3DS",
    city="Ottawa",
    province="ON",
    building_id="ibndsiufsd")

session = get_session()
sqlRepo = SqlAlchemyBuildingRepository(session)
print(sqlRepo.list())
# sqlRepo.add(building1)
# session.commit()
print(sqlRepo.get('ibndsiufsd').building_sections)


building_section = BuildingSection(2, floor=23,room=543)
session.add(building_section)
# session.commit()
