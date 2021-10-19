from config import Config
appconf = Config()
from db import session, initialize
from db.models import Kisi

initialize()