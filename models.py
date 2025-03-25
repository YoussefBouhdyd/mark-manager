from app import db

class marks(db.Model):
    id = db.Column(db.Integer,primary_key = True,autoincrement = True)
    student_name = db.Column(db.Text,nullable = False)
    math = db.Column(db.Float,nullable = False)
    computer = db.Column(db.Float,nullable = False)