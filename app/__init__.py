from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  
from flask_wtf.csrf import CSRFProtect 



app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
csrf = CSRFProtect(app)


# Instantiate Flask-Migrate here
migrate = Migrate(app, db)


from app import views
from app import models