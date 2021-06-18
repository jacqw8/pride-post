from pridepost import db

class Msg(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    msg = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return self.msg