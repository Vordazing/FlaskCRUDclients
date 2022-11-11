from flask import render_template, redirect
from .forms import AddEquipment
from sweater import app, db
from sweater.models import Customer, Technical, Equipment_accounting


@app.route('/equipment_add', methods=['GET', 'POST'])
def addEquipment():
    formcequipmentadd = AddEquipment()
    formcequipmentadd.client_id.choices = [(Customers.id, Customers.surname) for Customers in
                                       Customer.query.all()]

    formcequipmentadd.technical_id.choices = [(Technicals.id_technical_list, Technicals.model) for Technicals in
                                       Technical.query.all()]

    if formcequipmentadd.validate_on_submit():
        new_equipmentadd = Equipment_accounting(serial_number=formcequipmentadd.serial_number.data, client_id=formcequipmentadd.client_id.data, technical_id=formcequipmentadd.technical_id.data)
        db.session.add(new_equipmentadd)
        db.session.commit()
        return redirect('/equipment_add')

    return render_template('equipment_add.html', formequipmentadd=formcequipmentadd)