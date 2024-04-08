from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  
from flask_wtf.csrf import CSRFProtect 
from flask_cors import CORS  # Import CORS from flask_cors



app = Flask(__name__)
app.config.from_object(Config)

CORS(app)
db = SQLAlchemy(app)
csrf = CSRFProtect(app)


# Instantiate Flask-Migrate here
migrate = Migrate(app, db)


from app import views
from app import models