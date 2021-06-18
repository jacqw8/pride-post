from flask import render_template, url_for, flash, redirect, request, send_from_directory, Response, jsonify, abort


@app.route("/", methods=['GET'])
def index():
    return render_template('index.html', title='Index')


