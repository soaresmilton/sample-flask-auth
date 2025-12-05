from app import db


class User(db.Model):
    # id (int), username (string), password(string)
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)

    
    def __init__(self):
        super().__init__()