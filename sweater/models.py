
from flask_login import UserMixin
from sweater import db, login_manager
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)


class Customer(db.Model):
    __tablename__ = 'customer'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    surname = db.Column(db.String(255), nullable=False)
    debt = db.Column(db.NUMERIC, nullable=False)
    last_account = db.Column(db.NUMERIC, nullable=False)
    last_bill_of_the_month = db.Column(db.DATETIME, nullable=False)
    rate = db.Column(db.NUMERIC, nullable=False)

    condition_id = db.Column(db.Integer, db.ForeignKey('condition.id_condition'), nullable=False)
    status_id = db.Column(db.Integer, db.ForeignKey('status.id_status'), nullable=False)
    payment_method_id = db.Column(db.Integer, db.ForeignKey('payment_method.id_payment_method'), nullable=False)
    payment_type_id = db.Column(db.Integer, db.ForeignKey('payment_type.id_payment_type'), nullable=False)

    egu_1 = db.relationship('Equipment_accounting', backref='customer', lazy=True)


class Condition(db.Model):
    __tablename__ = 'condition'
    id_condition = db.Column(db.Integer, primary_key=True)
    list_condition = db.Column(db.String, nullable=False)
    cust_1 = db.relationship('Customer', backref='condition', lazy=True)


class Status(db.Model):
    __tablename__ = 'status'
    id_status = db.Column(db.Integer, primary_key=True)
    list_status = db.Column(db.String, nullable=False)
    cust_2 = db.relationship('Customer', backref='status', lazy=True)


class Payment_method(db.Model):
    __tablename__ = 'payment_method'
    id_payment_method = db.Column(db.Integer, primary_key=True)
    list_payment_method = db.Column(db.String, nullable=False)
    cust_3 = db.relationship('Customer', backref='payment_method', lazy=True)


class Payment_type(db.Model):
    __tablename__ = 'payment_type'
    id_payment_type = db.Column(db.Integer, primary_key=True)
    list_payment_type = db.Column(db.String, nullable=False)
    cust_4 = db.relationship('Customer', backref='payment_type', lazy=True)


class Done_accounts(db.Model):
    __tablename__ = 'done_accounts'
    id_done_accounts = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, nullable=False)
    after = db.Column(db.Integer, nullable=False)
    result = db.Column(db.String, nullable=False)

    model = db.Column(db.String, nullable=False)
    consumption = db.Column(db.Float, nullable=False)
    start_of_placement = db.Column(db.Integer, nullable=False)
    end_of_placement = db.Column(db.Integer, nullable=False)
    simple_in_hours = db.Column(db.Integer, nullable=False)
    number_of_cars = db.Column(db.Integer, nullable=False)
    result_day = db.Column(db.String, nullable=False)

    date = db.Column(db.DATETIME, default=datetime.utcnow)
    time = db.Column(db.DATETIME, default=datetime.now)


class Equipment_accounting(db.Model):
    __tablename__ ='equipment_accounting'
    id_equipment_accounting = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DATETIME, default=datetime.utcnow)
    serial_number = db.Column(db.String, nullable=False)

    client_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    technical_id = db.Column(db.Integer, db.ForeignKey('technical_info.id_technical_list'), nullable=False)


class Technical(db.Model):
    __tablename__ = 'technical_info'
    id_technical_list = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String, nullable=False)
    egu_2 = db.relationship('Equipment_accounting', backref='technical_info', lazy=True)







