from flask import render_template, url_for, flash, redirect, request, send_from_directory, Response, jsonify, abort
from pridepost import app
from pridepost import analysis
from pridepost.forms import ReusableForm

@app.route("/", methods=['GET', 'POST'])
def index():
    form = ReusableForm()
    return render_template('index.html', title='Index')


