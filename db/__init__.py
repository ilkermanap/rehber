from app import  appconf
import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
engine = create_engine(appconf.SQLALCHEMY_DATABASE_URI)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()



def initialize():
    if os.path.isfile(appconf.SQLALCHEMY_DATABASE_FILE) == False:
        print("Database table creation")
        # Motoru kullanarak tablolari yarat. 
        Base.metadata.create_all(engine)


