from flask import render_template, request
from sqlalchemy import or_


from sweater.models import Summary_all_filter
from sweater import app


@app.route('/summary', methods=['GET', 'POST'], defaults={"page": 1})
@app.route('/<int:page>', methods=['GET', 'POST'])
def summary(page):
    pages = 15
    tag = request.form.get('search') or request.args.get('tag')
    search = "%{}%".format(tag)
    if tag is not None:
        page = page if tag.startswith('%') else 1
        tag = tag if tag.startswith('%') else f'%{tag}%'

        saf = Summary_all_filter.query.order_by(Summary_all_filter.source).filter(or_(Summary_all_filter.serial_number.like(search), Summary_all_filter.source.like(search), Summary_all_filter.object.like(search),
                                                                                            Summary_all_filter.hostname.like(search), Summary_all_filter.worker.like(search), Summary_all_filter.ip_addres.like(search),
                                                                                            Summary_all_filter.model.like(search), Summary_all_filter.owner.like(search), Summary_all_filter.redirect.like(search))).paginate(per_page=pages, page=page, error_out=False)
        return render_template('summary.html', result=saf, tag=tag)

    summary_all = Summary_all_filter.query.order_by(Summary_all_filter.source).paginate(per_page=pages, page=page, error_out=False)
    return render_template('summary.html', result=summary_all)


