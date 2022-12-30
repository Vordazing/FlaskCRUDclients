import sqlalchemy
from flask import render_template, request
from sqlalchemy import or_, cast, and_


from sweater.models import ChronolZlat1, ChronolZlat2, ChronolZlat3, ChronolIrk1
from sweater import app


@app.route('/chronology', methods=['GET', 'POST'])
def chronology():
    return render_template('chronology.html')


@app.route('/chronolzlat1', methods=['GET', 'POST'], defaults={"page": 1})
@app.route('/chronolzlat1/<int:page>', methods=['GET', 'POST'])
def chronolzlat1(page):
    title = 'Chronol Zlat 1'
    pages = 15
    tag_1 = request.form.get('search') or request.args.get('tag_1')
    search = "%{}%".format(tag_1)
    if tag_1 is not None:
        page = page if tag_1.startswith('%') else 1
        tag_1 = tag_1 if tag_1.startswith('%') else f'%{tag_1}%'

        cz1 = ChronolZlat1.query.order_by(ChronolZlat1.date.desc()).filter(or_(ChronolZlat1.serial_number.like(search), ChronolZlat1.owner.like(search),
                ChronolZlat1.redirect.like(search))).paginate(per_page=pages, page=page, error_out=False)
        return render_template('chronolobject_1.html', result=cz1, tag=tag_1, title=title)

    chron = ChronolZlat1.query.order_by(ChronolZlat1.date.desc()).paginate(per_page=pages, page=page, error_out=False)
    return render_template('chronolobject_1.html', result=chron, title=title)


@app.route('/chronolzlat2', methods=['GET', 'POST'], defaults={"page": 1})
@app.route('/chronolzlat2/<int:page>', methods=['GET', 'POST'])
def chronolzlat2(page):
    title = 'Chronol Zlat 2'
    pages = 15
    tag_2 = request.form.get('search') or request.args.get('tag')
    search = "%{}%".format(tag_2)
    if tag_2 is not None:
        page = page if tag_2.startswith('%') else 1
        tag_2 = tag_2 if tag_2.startswith('%') else f'%{tag_2}%'

        cz2 = ChronolZlat2.query.order_by(ChronolZlat2.date.desc()).filter(or_(ChronolZlat2.serial_number.like(search), ChronolZlat2.owner.like(search),
                ChronolZlat2.redirect.like(search))).paginate(per_page=pages, page=page, error_out=False)
        return render_template('chronolobject_2.html', result=cz2, tag=tag_2, title=title)

    chron = ChronolZlat2.query.order_by(ChronolZlat2.date.desc()).paginate(per_page=pages, page=page, error_out=False)
    return render_template('chronolobject_2.html', result=chron, title=title)


@app.route('/chronolzlat3', methods=['GET', 'POST'], defaults={"page": 1})
@app.route('/chronolzlat3/<int:page>', methods=['GET', 'POST'])
def chronolzlat3(page):
    title = 'Chronol Zlat 3'
    pages = 15
    tag_3 = request.form.get('search') or request.args.get('tag')
    search = "%{}%".format(tag_3)
    if tag_3 is not None:
        page = page if tag_3.startswith('%') else 1
        tag_3 = tag_3 if tag_3.startswith('%') else f'%{tag_3}%'

        cz3 = ChronolZlat3.query.order_by(ChronolZlat3.date.desc()).filter(or_(ChronolZlat3.serial_number.like(search), ChronolZlat3.owner.like(search),
                ChronolZlat3.redirect.like(search))).paginate(per_page=pages, page=page, error_out=False)
        return render_template('chronolobject_3.html', result=cz3, tag=tag_3, title=title)

    chron = ChronolZlat3.query.order_by(ChronolZlat3.date.desc()).paginate(per_page=pages, page=page, error_out=False)
    return render_template('chronolobject_3.html', result=chron, title=title)


@app.route('/chronolirk1', methods=['GET', 'POST'], defaults={"page": 1})
@app.route('/chronolirk1/<int:page>', methods=['GET', 'POST'])
def chronolirk1(page):
    title = 'Chronol Irk 1'
    pages = 15
    tag_4 = request.form.get('search') or request.args.get('tag')
    search = "%{}%".format(tag_4)
    if tag_4 is not None:
        page = page if tag_4.startswith('%') else 1
        tag_4 = tag_4 if tag_4.startswith('%') else f'%{tag_4}%'

        ci1 = ChronolIrk1.query.order_by(ChronolIrk1.date.desc()).filter(or_(ChronolIrk1.serial_number.like(search), ChronolIrk1.owner.like(search),
                ChronolIrk1.redirect.like(search))).paginate(per_page=pages, page=page, error_out=False)
        return render_template('chronolobject_4.html', result=ci1, tag=tag_4, title=title)

    chron = ChronolIrk1.query.order_by(ChronolIrk1.date.desc()).paginate(per_page=pages, page=page, error_out=False)
    return render_template('chronolobject_4.html', result=chron, title=title)