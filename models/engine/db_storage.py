#!/usr/bin/python3
from os import environ

from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from models.base_model import Base
from models.city import City
from models.state import State


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        if (environ.get("HBNB_ENV") == "test"
                and self.__engine is not None):
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
        temp = {}
        if cls is None:
            classes = [City, State]
            for _cls in classes:
                rows = self.session.query(_cls).all()
                for row in rows:
                    key = f"{type(row).__name__}.{row.id}"
                    temp[key] = row
        else:
            queries = self.session.query(cls).all()
            for obj in queries:
                key = f"{obj.__class__.__name__}.{obj.id}"
                temp[key] = obj
        return temp

    def new(self, obj):
        self.session.add(obj)

    def save(self):
        self.session.commit()

    def delete(self, obj=None):
        if obj:
            self.session.delete(obj)

    def reload(self):
        from models.city import City
        from models.state import State
        from models.user import User
        from models.place import Place
        from models.review import Review

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    @property
    def session(self):
        return self.__session
