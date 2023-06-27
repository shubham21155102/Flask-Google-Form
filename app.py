from flask import Flask, render_template, request,redirect,url_for,jsonify
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        roll = request.form.get('roll')
        branch = request.form.get('branch')
        year = request.form.get('year')
        dob = request.form.get('dob')

        sender_email = "resoshubham2002@gmail.com"
        receiver_email = email
        password = "vwwpdhyibyjzzkbg"
        subject = "Form Submitted"
        message = "Thanks for submission"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(sender_email, password)

            email_message = MIMEMultipart()
            email_message["From"] = sender_email
            email_message["To"] = receiver_email
            email_message["Subject"] = subject

            email_message.attach(MIMEText(message, "plain"))

            connection.send_message(email_message)

        return render_template('response.html', name=name, email=email, roll=roll, branch=branch, year=year, dob=dob)

    return render_template('form.html')

import sqlite3

@app.route("/save", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        roll = request.form.get("roll")
        branch = request.form.get("branch")
        year = request.form.get("year")
        dob = request.form.get("dob")

        with sqlite3.connect('data.db') as conn:
            c = conn.cursor()
            c.execute("INSERT INTO formdata(name, email, roll, branch, year, dob) VALUES (?, ?, ?, ?, ?, ?)",
                      (name, email, roll, branch, year, dob))
            conn.commit()
        return render_template("response.html", name=name, email=email, roll=roll, branch=branch, year=year, dob=dob)

    return render_template("form.html")
@app.route('/alldatas')
def render_alldatas():
    with sqlite3.connect('data.db') as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM formdata")
        data = c.fetchall()
        # Retrieve column names
        column_names = [desc[0] for desc in c.description]
    json_data = [dict(zip(column_names, row)) for row in data]
    return jsonify(json_data)
@app.route("/displayall")
def displayall():
    with sqlite3.connect('data.db') as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM formdata")
        data = c.fetchall()
    return render_template("alldatas.html", data=data)
if __name__ == '__main__':
    app.run(debug=True)
