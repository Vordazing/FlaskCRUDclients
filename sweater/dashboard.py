from flask import render_template
from sweater import app
from flask_login import login_required


@app.route('/dashboard', methods=['GET', 'POST'])
# @login_required
def dashboard():
    return render_template('dashboard.html')