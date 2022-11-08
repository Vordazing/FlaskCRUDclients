from flask import render_template
from sweater import app
from sweater.models import Customer


@app.route('/customer', methods=['GET', 'POST'])
def cust():
    customers = Customer.query.all()
    return render_template('customer.html', customers=customers)