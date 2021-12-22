#!/usr/bin/python3

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classList = {"BaseModel": BaseModel, "Amenity": Amenity, "City": City,
             "Place": Place, "Review": Review, "State": State, "User": User}

class DBStorage():
    __engine = None
    __session = None

    def __init__(self):
        """"""
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(user, password, host, database), pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)
    
    def all(self, cls=None):
        """this method return a dictionary of 
        all objects depending of the class name"""
        my_dict = {}
        for i in classList:
            if cls is None or cls is classList[i] or cls is i:
                objs = self.__session.query(classList[i]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    my_dict[key] = obj
        return my_dict
    
    def new(self, obj):
        """add the object to the current dtabase session"""
        self.__session.add(obj)
    
    def save(self):
        """"""""
        self.__session.commit()

    def delete(self, obj=None):
        """"""""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """"""""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        session = scoped_session(Session)
        self.__session = Session()
    