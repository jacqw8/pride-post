from flask import render_template, url_for, flash, redirect, request, send_from_directory, Response, jsonify, abort
from pridepost import app, db
from pridepost import analysis
from pridepost.forms import ReusableForm
from pridepost.models import Msg

@app.route("/", methods=['GET', 'POST'])
def index():
    form = ReusableForm()
    msgs = []
    if form.validate_on_submit():
        if analysis.get_sentiment(form.search.data) == "Positive":
            msg = Msg(msg=form.search.data)
            db.session.add(msg)
            db.session.commit()
        else:
            flash('Please write a kind message!')
    msgs = Msg.query.all()
    return render_template('index.html', form=form, msgs=msgs, title='Index')


