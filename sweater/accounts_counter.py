from flask import render_template, request, session
from sweater import app
from sweater.models import Customer, Done_accounts


@app.route('/accounts_counter', methods=["POST", "GET"])
def accounts_counter():
    client_id = session.get('id_client', None)
    client = Customer.query.get(client_id)
    val3 = client.rate
    accounts = Done_accounts.query.filter_by(client_id=client_id)
    if request.method == "POST":
        val1 = request.form["field1"]
        val2 = request.form["field2"]
        result = (int(val2) - int(val1)) * val3
        if request.form.get("add"):
            session['id_client_db'] = client_id
            session['after_db'] = int(val2)
            session['result_db'] = result
        return render_template('accounts_counter.html', client=client, client_id=client_id, accounts=accounts, val=result)
    return render_template('accounts_counter.html', client=client, client_id=client_id, accounts=accounts)

