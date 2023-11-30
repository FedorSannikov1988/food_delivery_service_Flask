from dotenv import load_dotenv
from loguru import logger
from flask import Flask
from app import db
import os


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
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY').encode('latin-1')

db.init_app(app)
