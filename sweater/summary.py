from flask import render_template, request
from sqlalchemy import or_

from sweater.models import Summary_all_filter
from sweater import app


@app.route('/summary', methods=['GET', 'POST'], defaults={"page": 1})
@app.route('/<int:page>/<text:tag>', methods=['GET', 'POST'])
def summary(page):
    page = page
    pages = 15
    summary_all = Summary_all_filter.query.order_by(Summary_all_filter.source).paginate(per_page=pages, page=page, error_out=False)
    if request.method == "POST" and 'search' in request.form:
        tag = request.form["search"]
        search = "%{}%".format(tag)
        print(tag)
        if search != '%%':

            saf = Summary_all_filter.query.order_by(Summary_all_filter.source).filter(or_(Summary_all_filter.serial_number.like(search), Summary_all_filter.source.like(search), Summary_all_filter.object.like(search),
                                                                                            Summary_all_filter.hostname.like(search), Summary_all_filter.worker.like(search), Summary_all_filter.ip_addres.like(search),
                                                                                            Summary_all_filter.model.like(search), Summary_all_filter.owner.like(search), Summary_all_filter.redirect.like(search))).paginate(per_page=pages, error_out=False)
        else:
            saf = Summary_all_filter.query.order_by(Summary_all_filter.source).paginate(per_page=pages,  error_out=False)

        return render_template('summary.html', result=saf, tag=search)

    return render_template('summary.html', result=summary_all)


