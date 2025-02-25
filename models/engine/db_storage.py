#!/usr/bin/python3
"""This module defines the DBStorage engine"""
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.exc import IntegrityError, OperationalError
from os import getenv


class DBStorage:
    """this class manages storage of hbnb models in a database"""

    __engine = None
    __session = None

    def __init__(self):
        """Initialize a new DBstorage instance"""
        hb_user = getenv("HBNB_MYSQL_USER")
        hb_pwd = getenv("HBNB_MYSQL_PWD")
        hb_host = getenv("HBNB_MYSQL_HOST")
        hb_db = getenv("HBNB_MYSQL_DB")
        hb_env = getenv("HBNB_ENV")

        self.__engine = create_engine(
            f"mysql+mysqldb://{hb_user}:{hb_pwd}@{hb_host}/{hb_db}",
            pool_pre_ping=True,
        )

        if hb_env == "test":
            Base.metadata.drop_all(self.__engine)

    def reload(self):
        """Creates all tables in the database and creates a new session"""
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(
            sessionmaker(bind=self.__engine, expire_on_commit=False)
        )
        self.__session = Session()

    def all(self, cls=None):
        """Queries all objs of certain class"""
        allClasses = [User, Place, State, City, Amenity, Review]
        result = {}
        if cls is not None:
            for obj in self.__session.query(cls).all():
                ClassName = obj.__class__.__name__
                keyName = ClassName + "." + obj.id
                result[keyName] = obj
        else:
            for clss in allClasses:
                for obj in self.__session.query(clss).all():
                    ClassName = obj.__class__.__name__
                    keyName = ClassName + "." + obj.id
                    result[keyName] = obj
        return result

    def new(self, obj):
        """adds a new obj to the current database session"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """commits all changes of the current databse session"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes obj from the current database session"""
        if obj:
            self.__session.delete(obj)

    def close(self):
        """Closes the current session"""
        self.__session.close()
