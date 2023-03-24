import csv
from cs50 import SQL
from flask import Flask, render_template, request, redirect, session
from helpers import login_required
import sqlite3

app = Flask(__name__)

people = []
db = SQL("sqlite:///patients.db")
# db.execute("ALTER TABLE users ADD COLUMN password TEXT NOT NULL")
# db.execute("CREATE TABLE tests (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, name TEXT NOT NULL, grop TEXT NOT NULL, price TEXT NOT NULL)")
data = db.execute("SELECT * FROM tests")

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = 'mahmoud'

@app.route("/")
@login_required
def home():
  name = db.execute("SELECT name FROM users WHERE id=?", session["user_id"][0]['id'])
  return render_template("index.html", id=name[0]['name'])


@app.route("/signup", methods=["GET", "POST"])
def signup():
  if request.method == "GET":
    return render_template("signup.html")
  
  name = request.form.get("name")
  if not name :
    return render_template("signup.html",c="برجاء كتابة الاسم")
  
  phone = request.form.get("phone")
  if not phone :
    return render_template("signup.html",c="برجاء كتابة رقم الهاتف")

  password = request.form.get("password")
  repassword = request.form.get("repassword")
  if not password or not repassword :
    return render_template("signup.html",c="برجاء كتابة الرقم السرى")
  
  if repassword != password:
    return render_template("signup.html",c="الرقم السرى غير متطابق")
  
  db.execute("INSERT INTO users (name, phone, password) VALUES (?, ?, ?)", name, phone, password)
  return redirect("/login")


@app.route("/login", methods=["GET", "POST"])
def login():
  session.clear()
  if request.method == "GET":
    return render_template("login.html")

  name = request.form.get("name")
  if not name :
    return render_template("login.html",c="برجاء كتابة الاسم")

  password = request.form.get("password")
  if not password :
    return render_template("login.html",c="برجاء كتابة الرقم السرى")

  chek = db.execute("SELECT name, password FROM users")
  if name != chek[0]['name'] and password != chek[0]['password']:
    return render_template("login.html",c="الاسم او الرقم السرى خطا")

  user_id = db.execute("SELECT id FROM users WHERE name = ?", name)
  session["user_id"] = user_id
  return redirect("/")


@app.route("/result", methods=["GET", "POST"])
@login_required
def result():
  if request.method == "GET":
    return render_template("result.html")
  name = request.form.get("name")
  return render_template("results.html",names=data)


@app.route("/family", methods=["GET", "POST"])
@login_required
def family():
  if request.method == "GET":
    return render_template("family.html")
  name = request.form.get("name")
  relasion = request.form,get("relasion")
  return redirect("/")


@app.route("/visit", methods=["GET", "POST"])
@login_required
def visit():
  if request.method == "GET":
    tests = db.execute("SELECT * FROM tests")
    return render_template("visit.html", tests=tests)

# @app.route("/night")
# @login_required
# def night():
#   return render_template("index.html", night=night)
@app.route("/logout")
def logout():
  session.clear()
  return redirect ("/")
