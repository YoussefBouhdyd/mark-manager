from flask import render_template,request,make_response,flash,redirect,session,url_for
from models import marks

def register_routes(app,db):
    @app.route("/",methods=["POST","GET"])
    def index():
        if request.method == "GET":
            if request.cookies.get("login"):
                return redirect(url_for("calc"))
            return render_template("index.html")
        elif request.method == "POST":
            user_name = request.form.get("user-name")
            password = request.form.get("password")
            remember_me = request.form.get("remember")
            if (user_name == "Youssef" and password == "A@youssef123"):
                response = make_response(redirect(url_for("calc")))
                if remember_me == "on":
                    response.set_cookie("login",user_name)
                return response
            else:
                flash("Incorrect password or username !","login-alert")
                return redirect("/")

    @app.route("/calc",methods=["POST","GET"])
    def calc():
        if request.method == "GET" and request.cookies.get("login"):
            return render_template("calc.html")
        elif request.method == "POST":
            student_name = request.form.get("student-name")
            si = request.form.get("si")
            ro = request.form.get("ro")
            compilation = request.form.get("compilation")
            oop = request.form.get("oop")
            networking = request.form.get("networking")
            data_base = request.form.get("data-base")
            result = round((float(si) + float(ro) + float(compilation) + float(oop) + float(networking) + float(data_base)) / 8,2)
            return render_template("result.html",student = student_name, si = si , ro = ro , compilation = compilation , oop = oop , networking = networking , data_base = data_base,result = result)
        else:
            return redirect("/")

    @app.route("/log-out",methods = ["GET"])
    def log_out():
        response = make_response(redirect(url_for("index")))
        response.delete_cookie("login");
        return response

