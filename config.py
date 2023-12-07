from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from dotenv import load_dotenv
from flask_mail import Mail, \
                       Message
from loguru import logger
from flask import Flask
import os


LOWER_AGE_YEARS: int = 18
UPPER_AGE_YEARS: int = 100
TIME_TO_ACTIVATE_ACCOUNT_HOURS: int = 24


logger.add('logs/logs.json',
           level='DEBUG',
           format='{time} {level} {message}',
           rotation='10 MB',
           compression='zip',
           serialize=True)

app = Flask(__name__,
            template_folder='app/templates',
            static_folder='app/static')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY').encode('latin-1')
app.config['SECRET_KEY'] = SECRET_KEY

app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT'))
app.config['MAIL_USE_TLS'] = bool(os.getenv('MAIL_USE_TLS'))
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')

db = SQLAlchemy()
mail = Mail(app)
db.init_app(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
