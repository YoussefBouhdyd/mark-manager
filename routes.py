from flask import render_template,request,make_response,flash,redirect,session,url_for
from werkzeug.security import generate_password_hash, check_password_hash
from models import Marks,Teacher

def register_routes(app,db):
    @app.template_filter('trim')
    def trim_zero(n):
        return format(n,'g')
    
    @app.route("/sign-up" , methods = ["POST" , "GET"])
    def sign_up():
        if request.method == "POST":
            first_name = request.form.get('first-name')
            username = request.form.get('user-name')
            password = request.form.get('password')
            teacher = Teacher(teacher_name = first_name , username = username , password = generate_password_hash(password))
            db.session.add(teacher)
            db.session.commit()
            flash("You Registered Successfully","register-success")
            return redirect("/")

        return render_template("signUp.html")

    @app.route("/",methods=["POST","GET"])
    def index():
        if request.method == "GET":
            if request.cookies.get("login"):
                return redirect("/dashboard")
            return render_template("index.html")
        elif request.method == "POST":
            user_name = request.form.get("user-name")
            password = request.form.get("password")
            remember_me = request.form.get("remember")
            teacher = Teacher.query.filter_by(username = user_name).first()
            if teacher and check_password_hash(teacher.password,password):
                session['username'] = user_name
                response = make_response(redirect("/dashboard"))
                if remember_me == "on":
                    response.set_cookie("login",user_name)
                return response
            else:
                flash("Incorrect password or username !","login-alert")
                return redirect("/")

    @app.route("/dashboard")
    def dashboard():
        teacher_id = Teacher.query.filter_by(username =  session['username']).first().id_teacher
        records = Marks.query.filter_by(id_teacher = teacher_id).all()
        return render_template("dashboard.html",records=records)

    @app.route("/add",methods=["POST"])
    def add():
        student_name = request.form.get("student-name")
        math = request.form.get("math")
        computer = request.form.get("info")
        teacher_id = Teacher.query.filter_by(username = session['username']).first().id_teacher
        new_record = Marks(id_teacher = teacher_id,student_name=student_name, math=math, computer=computer)
        db.session.add(new_record)
        db.session.commit()
        return redirect("/dashboard")
    
    @app.route("/delete")
    def delete():
        student_id = request.args.get("id")
        student = Marks.query.get(student_id)
        db.session.delete(student)
        db.session.commit()
        return redirect("/dashboard")

    @app.route("/log-out",methods = ["GET"])
    def log_out():
        response = make_response(redirect(url_for("index")))
        response.delete_cookie("login")
        return response

    @app.route("/update",methods = ["POST"])
    def update():
        id = request.form.get('id')
        new_name = request.form.get('name-update')
        new_math = request.form.get('math-update')
        new_info = request.form.get('info-update')
        student = Marks.query.get(id)
        if student:
            student.student_name = new_name
            student.math = new_math
            student.computer = new_info
            db.session.commit()
        return redirect('/')
