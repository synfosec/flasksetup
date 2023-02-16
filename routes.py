from flask import Flask, Blueprint, render_template, url_for, redirect, request, flash, session

views = Blueprint("views",__name__)

@views.route("/")
def homepage():
    return render_template("index.html")
