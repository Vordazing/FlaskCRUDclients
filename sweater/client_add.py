from flask import render_template, redirect
from .forms import AddClient
from sweater import app, db
from sweater.models import Customer, Condition, Status, Payment_method, Payment_type


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

