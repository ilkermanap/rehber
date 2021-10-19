import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object): 
    SQLALCHEMY_DATABASE_FILE = os.path.join(basedir, 'app.db')  
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + SQLALCHEMY_DATABASE_FILE
    #SQLALCHEMY_DATABASE_URI = 'postgresql://username:passwd@localhost:5432/dbname'
