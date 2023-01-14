from flask import Flask, Blueprint, render_template, url_for, redirect, request, flash, session
from routes import views

app = Flask(__name__)
app.secret_key = "secret_key"
app.register_blueprint(views,url_prefix="/")

if __name__ == '__main__':
    app.run(debug=True)
