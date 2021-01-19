from flask import Flask, redirect, url_for, render_template, request, session, flash

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/register")
def register():
    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)