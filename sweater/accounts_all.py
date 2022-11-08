from flask import render_template, url_for, redirect, request, session
from sweater import app
from sweater.models import Customer



@app.route('/accounts_all', methods=['GET', 'POST'])
def accounts_all():

    all = Customer.query.all()

    if request.method == 'POST':
        operation = request.form['operation']
        client = request.form.get('client')
        part = client.split()
        name = part[0]
        surname = part[1]
        id_client = Customer.query.filter_by(name=name, surname=surname).first()

        if operation == 'accounts1':
            session['id_client'] = id_client.id
            return redirect(url_for('accounts_normal'))
        elif operation == 'accounts2':
            session['id_client'] = id_client.id
            return redirect(url_for('accounts_counter'))
        else:
            return redirect('/accounts_all')

    return render_template('accounts_all.html', all=all)