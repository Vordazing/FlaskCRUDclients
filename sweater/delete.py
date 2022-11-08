from flask import redirect
from sweater import app, db
from sweater.models import Customer


@app.route('/customer/<int:id>/del', methods=['GET', 'POST'])
def cust_del(id):
    customer = Customer.query.get_or_404(id)
    try:
        db.session.delete(customer)
        db.session.commit()
        return redirect("/customer")
    except:
        return "Error"