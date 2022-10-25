from flask import Flask, render_template, url_for, redirect
from flask_bcrypt import Bcrypt
from flask_login import login_user, login_required, logout_user
from .forms import LoginFrom, RegisterForm, AddClient

from sweater import app, db
from sweater.models import Users, Customer, Condition, Status, Payment_method, Payment_type


bcrypt = Bcrypt(app)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginFrom()
    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('dashboard'))
    return render_template('login.html', form=form)


@app.route('/dashboard', methods=['GET', 'POST'])
#@login_required
def dashboard():
    return render_template('dashboard.html')


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        new_user = Users(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('register.html', form=form)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('page404.html'), 404


@app.route('/customer', methods=['GET', 'POST'])
def cust():
    customers = Customer.query.all()
    return render_template('customer.html', customers=customers)


@app.route('/addclient', methods=['GET', 'POST'])
def addclient():
    formClient = AddClient()
    formClient.condition_id.choices = [(conditions.id_condition, conditions.list_condition) for conditions in
                                       Condition.query.all()]
    formClient.status_id.choices = [(statuses.id_status, statuses.list_status) for statuses in
                                    Status.query.all()]
    formClient.payment_method_id.choices = [(payment_methods.id_payment_method, payment_methods.list_payment_method) for
                                            payment_methods in
                                            Payment_method.query.all()]
    formClient.payment_type_id.choices = [(payment_types.id_payment_type, payment_types.list_payment_type) for
                                          payment_types in
                                          Payment_type.query.all()]

    if formClient.validate_on_submit():



        new_client = Customer(name=formClient.name.data, surname=formClient.surname.data, debt=formClient.debt.data,
                              last_account=formClient.last_account.data, rate=formClient.rate.data,
                              condition_id=formClient.condition_id.data, status_id=formClient.status_id.data, payment_method_id=formClient.payment_method_id.data, payment_type_id=formClient.payment_type_id.data)

        db.session.add(new_client)
        db.session.commit()
        return redirect('/customer')

    return render_template('addclient.html', formclient=formClient)


@app.route('/customer/<int:id>', methods=['GET', 'POST'])
def cust_open(id):
    customer = Customer.query.get(id)
    return render_template('client_open.html', customer=customer)


