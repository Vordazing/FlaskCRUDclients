from flask import render_template
from sweater import app


@app.errorhandler(404)
def page_not_found(e):
    return render_template('page404.html'), 404


@app.errorhandler(500)
def server_error(error):
    return render_template("page500.html", error=error)