import abc

from building.domain.model import Building, LeadData, AcmData, PcbData


class AbstractBuildingRepository(abc.ABC):

    @abc.abstractmethod
    def add(self, building: Building):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, building: str):
        raise NotImplementedError

    @abc.abstractmethod
    def list(self):
        raise NotImplementedError


class AbstractDataRepository(abc.ABC):

    @abc.abstractmethod
    def add(self, data):
        raise NotImplementedError

    @abc.abstractmethod
    def list_by_building_section(self, building_section_id: str):
        raise NotImplementedError

    @abc.abstractmethod
    def list(self):
        raise NotImplementedError


class SqlAlchemyBuildingRepository(AbstractBuildingRepository):

    def __init__(self, session):
        self.session = session

    def get(self, building_id: str):
        return self.session.query(Building).filter_by(building_id=building_id).one()

    def add(self, building: Building):
        self.session.add(building)

    def list(self):
        return self.session.query(Building).all()


class SqlAlchemyLeadDataRepository(AbstractDataRepository):
    def __init__(self, session):
        self.session = session

    def list_by_building_section(self, building_section_id: str):
        return self.session.query(LeadData).filter_by(building_section_id=building_section_id).all()

    def add(self, data: LeadData):
        self.session.add(data)

    def list(self):
        return self.session.query(LeadData).all()


class SqlAlchemyAcmDataRepository(AbstractDataRepository):
    def __init__(self, session):
        self.session = session

    def list_by_building_section(self, building_section_id: str):
        return self.session.query(AcmData).filter_by(building_section_id=building_section_id).all()

    def add(self, data: AcmData):
        self.session.add(data)

    def list(self):
        return self.session.query(AcmData).all()


class SqlAlchemyPcbDataRepository(AbstractDataRepository):
    def __init__(self, session):
        self.session = session

    def list_by_building_section(self, building_section_id: str):
        return self.session.query(PcbData).filter_by(building_section_id=building_section_id).all()

    def add(self, data: PcbData):
        self.session.add(data)

    def list(self):
        return self.session.query(PcbData).all()




