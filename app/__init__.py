from flask import Flask
from .config import DevConfig

#Initializing the application
app = Flask(__name__)

#setting up configuration
app.config.from_objects(DevConfig)

from app import views