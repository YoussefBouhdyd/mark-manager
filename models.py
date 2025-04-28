from app import db

class Teacher(db.Model):
    __tablename__ = 'teachers'
    id_teacher = db.Column(db.Integer, primary_key = True , autoincrement = True)
    teacher_name = db.Column(db.Text , nullable = False)
    password = db.Column(db.Text , nullable = False)
    username = db.Column(db.Text , nullable = False)

class Marks(db.Model):
    __tablename__ = 'marks'
    id = db.Column(db.Integer,primary_key = True,autoincrement = True)
    id_teacher = db.Column(db.Integer, db.ForeignKey('teachers.id_teacher'))
    student_name = db.Column(db.Text,nullable = False)
    math = db.Column(db.Float,nullable = False)
    computer = db.Column(db.Float,nullable = False)