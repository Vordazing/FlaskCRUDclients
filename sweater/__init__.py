from flask import Flask, request
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://lord:123456789@185.93.110.129/UMC'
app.config['SQLALCHEMY_BINDS'] = {
    'chronol': 'postgresql://lord:123456789@185.93.110.129/testlab',

}
app.config['SECRET_KEY'] = 'thisisasecretkey'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


from sweater import models, views, menu, login, errors, register, customer, \
    client_add, client_open, update, done_add_db_counter, done_add_db_normal, \
    accounts_counter, accounts_normal, accounts_all, equipment_add, summary, chronology