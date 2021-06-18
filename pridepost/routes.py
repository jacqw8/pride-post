from flask import render_template, url_for, flash, redirect, request, send_from_directory, Response, jsonify, abort
from pridepost import app
from pridepost import analysis
from pridepost.forms import ReusableForm

@app.route("/", methods=['GET', 'POST'])
def index():
    form = ReusableForm()
    if form.validate_on_submit():
        if analysis.get_sentiment(form.search.data) == "Positive":
            msg = Msg(msg=form.search.data)
            db.session.add(msg)
            db.session.commit()
    msgs = Msg.query.all()
    return render_template('index.html', form=form, msgs=msgs, title='Index')


