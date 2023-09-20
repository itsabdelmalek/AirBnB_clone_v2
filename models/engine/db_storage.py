#!/usr/bin/python3
""" This module defines a class to manage DB storage for hbnb clone"""
from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker
from os import getenv

HBNB_MYSQL_USER = 'hbnb_dev'



class DBStorage():
    """ This class manages storage of hbnb models in DB """
    __engine = None
    __session = None

    def __init__(self):
        """ Initialize DBStorage instances"""
        hb_user = getenv("HBNB_MYSQL_USER")
        hb_pwd = getenv("HBNB_MYSQL_PWD")
        hb_host = getenv("HBNB_MYSQL_HOST")
        hb_db = getenv("HBNB_MYSQL_DB")
        hb_env = getenv("HBNB_ENV")
        
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
            hb_user, hb_pwd, hb_host, hb_db), pool_pre_ping=True)
        