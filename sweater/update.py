from flask import render_template, url_for, redirect, request, session
from .forms import UpdateClient
from sweater import app, db
from sweater.models import Customer, Condition, Status, Payment_method, Payment_type


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


