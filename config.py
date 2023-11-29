from dotenv import load_dotenv
from flask import Flask
from app import db
import os


app = Flask(__name__, template_folder='app/templates', static_folder='app/static')


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

load_dotenv()
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY').encode('latin-1')

#app.config['INSTANCE_PATH'] = 'app/instance'

db.init_app(app)