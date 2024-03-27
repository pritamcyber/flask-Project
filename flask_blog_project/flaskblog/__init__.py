from flask import Flask #the flash use for one time message to send on a html page
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager 
from flask_bcrypt import Bcrypt

import datetime
import config

app = Flask(__name__)


app.config['SECRET_KEY']= 'fc7896df363b4ea0506c8eb5224637f1'
login_managers = LoginManager(app)
login_managers.login_view  = 'login' # this willl sent the user to login page if he is not logedin any route which has login requried 
login_managers.login_message_category = 'info'
login_managers  
# login_managers

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['UPLOAD_FOLDER'] = '../static/profile_pic'

db = SQLAlchemy(app)
bcrypt  = Bcrypt()

from flaskblog import routs