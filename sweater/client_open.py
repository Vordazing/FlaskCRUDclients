from flask import render_template
from sweater import app
from sweater.models import Customer, Done_accounts, Equipment_accounting


@app.route('/customer/<int:id>', methods=['GET', 'POST'])
def cust_open(id):
    customer = Customer.query.get(id)
    accounts = Done_accounts.query.filter_by(client_id=id)
    equ = Equipment_accounting.query.filter_by(client_id=id)
    count_equipment = Equipment_accounting.query.filter_by(client_id=id).count()

    check = 0
    for data in accounts:
        check = data.after
        if check is not None:
            check = 1
        elif check is None:
            check = 2
        else:
            pass
    return render_template('client_open.html', customer=customer, accounts=accounts, check=check, equ=equ, count=count_equipment)

