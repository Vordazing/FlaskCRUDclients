from flask import render_template
from sweater import app, db
from sweater.models import Customer, Equipment_accounting
from sqlalchemy import func




@app.route('/customer', methods=['GET', 'POST'])
def cust():
    customers = Customer.query.order_by(Customer.surname).all()

    #result = db.session.query(Customer.id, Customer.surname, func.count(Customer.id).label("total_counts")).join(Equipment_accounting).group_by(Customer.id).order_by(Customer.surname).all()

    return render_template('customer.html', customers=customers, result='error')