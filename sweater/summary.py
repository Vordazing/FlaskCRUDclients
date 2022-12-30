import sqlalchemy
from flask import render_template, request
from sqlalchemy import or_, cast, and_


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


@app.route('/summary_filter', methods=['GET', 'POST'])
def summary_filter():
    search_1 = request.form.get('source')
    search_1_format = "%{}%".format(search_1)
    search_2 = request.form.get('object')
    search_2_format = "%{}%".format(search_2)
    search_3 = request.form.get('hostname')
    search_3_format = "%{}%".format(search_3)
    search_4 = request.form.get('ip_address')
    search_4_format = "%{}%".format(search_4)
    search_5 = request.form.get('mac_address')
    search_5_format = "%{}%".format(search_5)
    search_6 = request.form.get('serial_number')
    search_6_format = "%{}%".format(search_6)
    search_7 = request.form.get('worker')
    search_7_format = "%{}%".format(search_7)
    search_8 = request.form.get('owner')
    search_8_format = "%{}%".format(search_8)
    search_9 = request.form.get('redirect')
    search_9_format = "%{}%".format(search_9)
    search_10 = request.form.get('plata_no_repair')
    search_10_format = "%{}%".format(search_10)
    search_11 = request.form.get('plata_removed')
    search_11_format = "%{}%".format(search_11)
    search_12 = request.form.get('model')
    search_12_format = "%{}%".format(search_12)
    search_13 = request.form.get('сonsumption')
    search_13_format = "%{}%".format(search_13)


    saf = Summary_all_filter.query.order_by(Summary_all_filter.source).filter(and_(Summary_all_filter.source.like(search_1_format), Summary_all_filter.object.like(search_2_format), Summary_all_filter.hostname.like(search_3_format),
            Summary_all_filter.ip_addres.like(search_4_format), Summary_all_filter.mac_address.like(search_5_format),
            Summary_all_filter.serial_number.like(search_6_format), Summary_all_filter.worker.like(search_7_format),
            Summary_all_filter.owner.like(search_8_format), Summary_all_filter.redirect.like(search_9_format),
            Summary_all_filter.plata_no_repair.like(search_10_format), Summary_all_filter.plata_removed.like(search_11_format),
            Summary_all_filter.model.like(search_12_format), cast(Summary_all_filter.result_power, sqlalchemy.Text).like(search_13_format))).all()

    return render_template('summary_filter.html', result_2=saf)