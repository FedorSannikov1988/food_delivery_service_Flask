from app import db
from flask import Flask


app = Flask(__name__,
            template_folder='app/templates',
            static_folder='app/static')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
#app.config['INSTANCE_PATH'] = 'app/instance'
db.init_app(app)