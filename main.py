from sqlalchemy import create_engine
from adapters import orm
from sqlalchemy.orm import sessionmaker
import config


def init_engine_with_models():
    engine = create_engine(config.get_postgres_uri())
    orm.metadata.create_all(engine)
    return engine


# engine = init_engine_with_models()
orm.start_mappers()
get_session = sessionmaker(bind=init_engine_with_models())
get_session()
