from flask import render_template
from sweater import app
from flask_login import login_required


@app.route('/menu', methods=['GET', 'POST'])
def dashboard():
    return render_template('menu.html')