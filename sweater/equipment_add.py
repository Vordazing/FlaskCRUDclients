from flask import render_template, redirect, session, url_for
from flask_wtf import FlaskForm
from wtforms import FieldList, FormField, SubmitField
from .forms import AddEquipment
from sweater import app, db, request
from sweater.models import Equipment_accounting

@app.route('/equipment_add', methods=['GET', 'POST'])
def addEquipment():
    equ = Equipment_accounting.query.order_by(Equipment_accounting.date).all()
    return render_template('equipment_add.html',  equ=equ)


@app.route('/next_equipment_add', methods=['POST'])
def Next():
    if request.method == "POST":
        update = request.form['update']
        session['update'] = update
        return redirect('/next')


@app.route('/next', methods=['GET', 'POST'])
def return_form():

    u = session.get('update', None)
    update = int(u)

    class ToSend(FlaskForm):
        send = FieldList(FormField(AddEquipment), min_entries=update)
        submit = SubmitField('Next')

    forma = ToSend()

    if request.method == 'POST':
        for field in forma.send:

            new_equipment = Equipment_accounting(serial_number=field.serial_number.data, technical_id=field.technical_id.data, client_id=field.client_id.data)
            db.session.add(new_equipment)
            db.session.commit()

        return redirect('/equipment_add')

    return render_template('next.html', form=forma)



