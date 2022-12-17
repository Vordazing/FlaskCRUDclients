from flask import render_template, redirect, request
from flask_login import login_required

from .forms import AddClient
from sweater import app, db
from sweater.models import Customer, Condition, Status, Payment_method, Payment_type


@app.route('/client_add', methods=['GET', 'POST'])
@login_required
def addClient():
    form = AddClient()

    form.condition_id.choices = [(conditions.id_condition, conditions.list_condition) for conditions in
                                       Condition.query.all()]
    form.status_id.choices = [(statuses.id_status, statuses.list_status) for statuses in
                                    Status.query.all()]
    form.payment_method_id.choices = [(payment_methods.id_payment_method, payment_methods.list_payment_method) for
                                            payment_methods in
                                            Payment_method.query.all()]
    form.payment_type_id.choices = [(payment_types.id_payment_type, payment_types.list_payment_type) for
                                          payment_types in
                                          Payment_type.query.all()]

    if request.method == 'POST':
        new_client = Customer(name=form.name.data, surname=form.surname.data, rate=form.rate.data, debt=0, last_account=0,
                              condition_id=form.condition_id.data, status_id=form.status_id.data, payment_method_id=form.payment_method_id.data, payment_type_id=form.payment_type_id.data)
        db.session.add(new_client)
        db.session.commit()
        return redirect('/customer')

    return render_template('client_add.html', form=form)

