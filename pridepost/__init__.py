from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = "\x7f\xec6\x14_\x8a\x16\x0c\xe9\xe9\xd6b\x93\xe6\x11$\xe4\xf4\xf8\xd6\xad\x82Xn"

# db = SQLAlchemy(app)
# bcrypt = Bcrypt(app)

from pridepost import routes