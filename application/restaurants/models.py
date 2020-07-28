from application import db

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)
    address = db.Column(db.String(144), nullable=False)
    postcode = db.Column(db.Integer, nullable=False)
    city = db.Column(db.String(144), nullable=False)

    def __init__(self, name):
        self.name = name
        self.done = False