from flask import render_template,request,make_response,flash,redirect,session,url_for
from models import marks

def register_routes(app,db):
    @app.template_filter('trim')
    def trim_zero(n):
        return format(n,'g')
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
            if (user_name == "Youssef" and password == "A@youssef123"):
                response = make_response(redirect("/dashboard"))
                if remember_me == "on":
                    response.set_cookie("login",user_name)
                return response
            else:
                flash("Incorrect password or username !","login-alert")
                return redirect("/")

    @app.route("/dashboard")
    def dashboard():
        records = marks.query.all()
        return render_template("dashboard.html",records=records)


    @app.route("/add",methods=["POST"])
    def add():
        student_name = request.form.get("student-name")
        math = request.form.get("math")
        computer = request.form.get("info")
        new_record = marks(student_name=student_name, math=math, computer=computer)
        db.session.add(new_record)
        db.session.commit()
        return redirect("/dashboard")
    
    @app.route("/delete")
    def delete():
        student_id = request.args.get("id")
        student = marks.query.get(student_id)
        db.session.delete(student)
        db.session.commit()
        return redirect("/dashboard")

    @app.route("/log-out",methods = ["GET"])
    def log_out():
        response = make_response(redirect(url_for("index")))
        response.delete_cookie("login")
        return response

