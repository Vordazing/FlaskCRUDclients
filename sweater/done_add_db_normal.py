from flask import render_template, session
from flask_login import login_required

from sweater import app, db
from sweater.models import Done_accounts


@app.route('/done_add_db_normal', methods=["GET", "POST"])
@login_required
def done_normal():
    client_id_db = session.get('id_client_db', None)
    model = session.get('model', None)
    consumption = session.get('consumption', None)
    number_of_cars = session.get('number_of_cars', None)
    start_of_placement = session.get('start_of_placement', None)
    end_of_placement = session.get('end_of_placement', None)
    simple_in_hours = session.get('simple_in_hours', None)
    result_day = session.get('result_day', None)
    result = session.get('result', None)

    result = Done_accounts(client_id=client_id_db, model=model, consumption=consumption, start_of_placement=start_of_placement, end_of_placement=end_of_placement, simple_in_hours=simple_in_hours, number_of_cars=number_of_cars, result_day=result_day, result=result)
    db.session.add(result)
    db.session.commit()

    session.clear()


    return render_template('done_db.html')

