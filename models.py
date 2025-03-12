from app import db

class marks(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    student_name = db.Column(db.Text,nullable = False)
    oop = db.Column(db.Float,nullable = False)
    ro = db.Column(db.Float,nullable = False)
    net = db.Column(db.Float,nullable = False)
    comp = db.Column(db.Float,nullable = False)
    database = db.Column(db.Float,nullable = False)
    si = db.Column(db.Float,nullable = False)