from os import environ

from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from models.base_model import Base


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        if environ.get("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'
            .format(
                environ["HBNB_MYSQL_USER"],
                environ["HBNB_MYSQL_PWD"],
                environ["HBNB_MYSQL_HOST"],
                environ["HBNB_MYSQL_DB"]
            ), pool_pre_ping=True
        )
        self.__session = sessionmaker(bind=self.__engine)

    def all(self, cls=None) -> dict:
        from models.base_model import BaseModel
        temp = {}
        if cls == None:
            classes = [v.__name__ for v in BaseModel.__subclasses__()]
            queries = self.session.query(*classes)
        else:
            queries = self.session.query(*cls)

        for obj in queries:
            key = f"{obj.__class__}.{obj.id}"
            temp[key] = obj
        return temp

    def new(self, obj):
        self.session.add(obj)

    def save(self):
        self.session.commit()

    def delete(self, obj=None):
        if obj:
            self.session.query(obj).delete()

    def reload(self):
        from models.city import City
        from models.state import State
        from models.user import User

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    @property
    def session(self):
        return self.__session
