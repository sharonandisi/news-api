from flask import Flask
from .config import DevConfig

#Initializing the application
app = Flask(__name__,instance_relative_config= True)

#setting up configuration
app.config.from_objects(DevConfig)
app.config.from_pylife('config.py')

from app import views