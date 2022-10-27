from flask import Flask, render_template, url_for, redirect, request
from flask_bcrypt import Bcrypt
from flask_login import login_user, login_required, logout_user
from .forms import LoginFrom, RegisterForm, AddClient, UpdateClient

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


@app.route('/client_add', methods=['GET', 'POST'])
def addclient():
    formclientadd = AddClient()
    formclientadd.condition_id.choices = [(conditions.id_condition, conditions.list_condition) for conditions in
                                       Condition.query.all()]
    formclientadd.status_id.choices = [(statuses.id_status, statuses.list_status) for statuses in
                                    Status.query.all()]
    formclientadd.payment_method_id.choices = [(payment_methods.id_payment_method, payment_methods.list_payment_method) for
                                            payment_methods in
                                            Payment_method.query.all()]
    formclientadd.payment_type_id.choices = [(payment_types.id_payment_type, payment_types.list_payment_type) for
                                          payment_types in
                                          Payment_type.query.all()]

    if formclientadd.validate_on_submit():
        new_client = Customer(name=formclientadd.name.data, surname=formclientadd.surname.data, debt=formclientadd.debt.data,
                              last_account=formclientadd.last_account.data, rate=formclientadd.rate.data,
                              condition_id=formclientadd.condition_id.data, status_id=formclientadd.status_id.data, payment_method_id=formclientadd.payment_method_id.data, payment_type_id=formclientadd.payment_type_id.data)
        db.session.add(new_client)
        db.session.commit()
        return redirect('/customer')

    return render_template('client_add.html', formclientadd=formclientadd)


@app.route('/customer/<int:id>', methods=['GET', 'POST'])
def cust_open(id):
    customer = Customer.query.get(id)
    return render_template('client_open.html', customer=customer)


@app.route('/customer/<int:id>/del', methods=['GET', 'POST'])
def cust_del(id):
    customer = Customer.query.get_or_404(id)
    try:
        db.session.delete(customer)
        db.session.commit()
        return redirect("/customer")
    except:
        return "Error"


@app.route('/customer/<int:id>/update', methods=['GET', 'POST'])
def cust_update(id):
    customer = Customer.query.get(id)
    formclientupdate = UpdateClient(obj=customer)

    formclientupdate.condition_id.choices = [(conditions.id_condition, conditions.list_condition) for conditions in
                                       Condition.query.all()]
    formclientupdate.status_id.choices = [(statuses.id_status, statuses.list_status) for statuses in
                                    Status.query.all()]
    formclientupdate.payment_method_id.choices = [(payment_methods.id_payment_method, payment_methods.list_payment_method) for
                                            payment_methods in
                                            Payment_method.query.all()]
    formclientupdate.payment_type_id.choices = [(payment_types.id_payment_type, payment_types.list_payment_type) for
                                          payment_types in
                                          Payment_type.query.all()]

    if formclientupdate.validate_on_submit():
        try:
            formclientupdate.populate_obj(customer)
            db.session.commit()
            return redirect("/customer")
        except:
            "Error"

    return render_template('client_update.html', formclientupdate=formclientupdate, customer=customer)





