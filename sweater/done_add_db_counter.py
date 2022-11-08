from flask import render_template, session
from sweater import app, db
from sweater.models import Done_accounts


@app.route('/done_add_db_counter', methods=["GET", "POST"])
def done_counter():
    client_id_db = session.get('id_client_db', None)
    after_db = session.get('after_db', None)
    result_db = session.get('result_db', None)

    result = Done_accounts(client_id=client_id_db, after=after_db, result=result_db)
    db.session.add(result)
    db.session.commit()

    return render_template('done_db.html')