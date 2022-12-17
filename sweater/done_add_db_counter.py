from flask import render_template, session
from flask_login import login_required

from sweater import app, db
from sweater.models import Done_accounts


@app.route('/done_add_db_counter', methods=["GET", "POST"])
@login_required
def done_counter():
    client_id_db = session.get('id_client_db', None)
    after_db = session.get('after_db', None)
    result_db = session.get('result_db', None)

    result = Done_accounts(client_id=client_id_db, after=after_db, result=result_db)
    db.session.add(result)
    db.session.commit()
    session.clear()



    return render_template('done_db.html')