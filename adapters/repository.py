import abc

from domain.model import Building, BuildingSection, PcbData, LeadData, AcmData


class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def add(self, building: Building):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, building: str):
        raise NotImplementedError

    @abc.abstractmethod
    def list(self):
        raise NotImplementedError


class SqlAlchemyBuildingRepository(AbstractRepository):

    def __init__(self, session):
        self.session = session

    def get(self, building_id: str):
        return self.session.query(Building).filter_by(building_id=building_id).one()

    def add(self, building: Building):
        self.session.add(building)

    def list(self):
        return self.session.query(Building).all()
