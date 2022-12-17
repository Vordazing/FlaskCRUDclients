from flask import render_template, redirect
from flask_login import login_required

from sweater import app, db
from sweater.models import Customer, Equipment_accounting
from sqlalchemy import func


@app.route('/customer', methods=['GET', 'POST'])
@login_required
def cust():
    customers = Customer.query.order_by(Customer.surname).all()

    #result = db.session.query(Customer.id, Customer.surname, func.count(Customer.id).label("total_counts")).join(Equipment_accounting).group_by(Customer.id).order_by(Customer.surname).all()

    return render_template('customer.html', customers=customers, result='error')



@app.route('/customer/<int:id>/del', methods=['GET', 'POST'])
def cust_del(id):
    customer = Customer.query.get_or_404(id)
    try:
        db.session.delete(customer)
        db.session.commit()
        return redirect("/customer")
    except:
        return "Error"