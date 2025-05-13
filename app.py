from flask import Flask, render_template, request
import os
import paramiko


app = Flask(__name__)
#pages

@app.route("/")
def immerse():
    return render_template("immerse.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/essays")
def essays():
    return render_template("essays.html")

@app.route("/future")
def future():
    return render_template("future.html")

@app.route("/intro")
def intro():
    return render_template("intro.html", title="intro")

@app.route("/growth")
def growth():
    return render_template("growth.html", title="growth")

@app.route("/works-cited")
def worksCited():
    return render_template("works-cited.html", title="works-cited")

@app.route("/contact")
def contact():
    return render_template("contact.html", title="Contact", content="<ol>My Email: wsnellings@atlantaacademy.com</ol>")



# you know what this is
if __name__ == '__main__':
    socketio.run(app, debug=True, port=os.getenv("PORT", default=5000))
