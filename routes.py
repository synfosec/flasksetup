from flask import Flask, Blueprint, render_template, url_for, redirect, request, flash, session

views = Blueprint("views",__name__)

@views.route("/")
def homepage():
    return "<h1>Hello, world!</h1>"
